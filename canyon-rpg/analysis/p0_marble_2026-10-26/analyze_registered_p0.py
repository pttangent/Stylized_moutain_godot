#!/usr/bin/env python3
"""Reproducible, metric-free review of user paired Marble landmarks and collider."""
import json, math
from pathlib import Path
import numpy as np
import trimesh
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from PIL import Image
ROOT=Path(__file__).resolve().parent
ASSET=Path(__file__).parents[2]/'assets/worlds/canyon-waterfall'
WORK=Path('/tmp/canyon_marble_p0_review_2026_10_26')
pairs=json.loads((ROOT/'annotations/paired_landmarks_user_reviewed.json').read_text())['pairs']
pd={p['id']:p for p in pairs if p.get('mesh_xyz_raw') is not None}
mesh=trimesh.load(ASSET/'canyon-waterfall-collider.glb',force='mesh')
cam=json.loads((ROOT/'registration/camera_registration_candidate.json').read_text())
rays=json.loads((ROOT/'registration/projected_landmarks_unverified.json').read_text())
rd={p['id']:p for p in rays['points']}
records=[]
for p in pairs:
 r={'id':p['id'],'kind':p['kind'],'pixel_xy':p['pixel_xy'],'reviewed_pair':bool(p.get('human_approved')),'raw_xyz':p.get('mesh_xyz_raw')}
 if p.get('mesh_xyz_raw') is not None:
  xyz=np.array(p['mesh_xyz_raw'],float);fi=p['face_index'];tri=mesh.faces[fi]
  n=mesh.face_normals[fi];rgb=mesh.visual.vertex_colors[tri,:3].mean(axis=0)
  hits=rd[p['id']]['candidate_hits'];hit_dist=[float(np.linalg.norm(xyz-np.array(h['point_raw_xyz']))) for h in hits]
  r.update(height_raw_units_minus_y=float(-xyz[1]),up_facing_normal_dot=float(-n[1]),face_mean_rgb=[round(float(c),1) for c in rgb],source_camera_candidate_hit_count=len(hits),nearest_source_camera_ray_hit_error_raw_units=min(hit_dist) if hit_dist else None,source_camera_ray_hit_errors_raw_units=hit_dist)
  r['semantic_status']='ANCHOR_HINT_ONLY_NOT_SURFACE_CLASSIFIED'
  if p['kind'] in ('water_reach','waterfall','pool') and rgb[1]>rgb[2]*1.13:r['semantic_review_flag']='WATER_HINT_ON_GREENISH_COLLIDER_FACE'
  if p['kind'] in ('terrace','path','path_waypoint') and -n[1]<.8:r['semantic_review_flag']='PATH_HINT_ON_SLOPED_OR_VERTICAL_FACE'
  if p['kind']=='stairs' and -n[1]<.8:r['semantic_review_flag']='STAIR_HINT_ON_STEEP_FACE'
 records.append(r)

def edges(domain,file):
 g=json.loads((WORK/'blueprint'/file).read_text());out=[]
 for e in g['edges']:
  a=pd.get(e['from']);b=pd.get(e['to']);o={'id':e['id'],'from':e['from'],'to':e['to'],'continuous_surface_tested':False,'semantic_classification_approved':False}
  if a and b:
   aa=np.array(a['mesh_xyz_raw']);bb=np.array(b['mesh_xyz_raw']);d=bb-aa;h=math.hypot(d[0],d[2]);dh=float(aa[1]-bb[1]) # minus-Y is up: h_start-h_end == bY-aY; corrected below
   # Height above datum = -rawY, so h_start-h_end = rawY_end - rawY_start.
   dh=float(bb[1]-aa[1]);o.update(distance_raw_units=float(np.linalg.norm(d)),horizontal_distance_raw_units=h,drop_start_to_end_raw_units=dh,endpoint_grade_ratio_abs=float(abs(dh)/h) if h else None,endpoint_angle_deg_abs=float(math.degrees(math.atan2(abs(dh),h))),status='ENDPOINTS_ONLY')
   if domain=='water' and dh<=0:o['status']='HEIGHT_DIRECTION_CONFLICT'
  else:o['status']='MISSING_3D_ENDPOINT'
  out.append(o)
 return out
water=edges('water','water_graph_proposed.json');nav=edges('navigation','navigation_graph_proposed.json')
# World-model axis evidence, independent of absolute metric scale.
water_known=[e for e in water if 'drop_start_to_end_raw_units' in e]
axis={'selected_up_axis_raw':'-Y','status':'EVIDENCE_SUPPORTED_RELATIVE_AXIS_NOT_METRIC_CALIBRATION','water_edges_positive':sum(e['drop_start_to_end_raw_units']>0 for e in water_known),'water_edges_measured':len(water_known),'mesh_face_normals_minus_y_gt_0p75':int((-mesh.face_normals[:,1]>.75).sum()),'mesh_face_normals_plus_y_gt_0p75':int((mesh.face_normals[:,1]>.75).sum()),'renderer_flip_x_180_makes_raw_minus_y_display_plus_y':True,'scale_m_per_raw_unit':None,'origin_raw_xyz':pd['bridge']['mesh_xyz_raw']}
# Dense colored top-down collider evidence, restricted to observed landmark neighbourhood.
cent=mesh.triangles_center;n=mesh.face_normals
col=mesh.visual.vertex_colors[mesh.faces,:3].mean(axis=1)/255
core=(cent[:,0]>-1.65)&(cent[:,0]<1.5)&(cent[:,2]>.75)&(cent[:,2]<5.1)&(cent[:,1]>-1.2)
fig,ax=plt.subplots(1,2,figsize=(19,10),constrained_layout=True)
img=Image.open(ASSET/'canyon-waterfall-reference.jpeg')
ax[0].imshow(img);ax[0].set_title('Reference image — user reviewed pixels, original 2752 × 1536')
for r in records:
 if not r['reviewed_pair']:continue
 x,y=r['pixel_xy'];ax[0].plot(x,y,'o',ms=4,color='yellow',mec='black',mew=.6);ax[0].annotate(r['id'],(x,y),xytext=(4,-4),textcoords='offset points',fontsize=6,color='white',bbox=dict(facecolor='black',alpha=.45,pad=1,edgecolor='none'))
ax[0].set_xlim(0,img.width);ax[0].set_ylim(img.height,0)
ax[1].scatter(cent[core,0],cent[core,2],c=col[core],s=1,alpha=.8,rasterized=True)
for r in records:
 if not r['reviewed_pair']:continue
 x,_,z=r['raw_xyz'];ax[1].plot(x,z,'o',ms=5,color='yellow',mec='black',mew=.7);ax[1].annotate(r['id'],(x,z),xytext=(3,3),textcoords='offset points',fontsize=6,bbox=dict(facecolor='white',alpha=.65,pad=1,edgecolor='none'))
for domain,es,color in [('water',water,'deepskyblue'),('navigation',nav,'orange')]:
 for e in es:
  if e['from'] not in pd or e['to'] not in pd:continue
  a=pd[e['from']]['mesh_xyz_raw'];b=pd[e['to']]['mesh_xyz_raw'];ax[1].plot([a[0],b[0]],[a[2],b[2]],color=color,alpha=.75,lw=1.3)
ax[1].set_title('Collider top view — raw X/Z, colors from GLB; lines are proposals')
ax[1].set_xlabel('raw X (not meters)');ax[1].set_ylabel('raw Z (not meters)');ax[1].set_aspect('equal');ax[1].grid(alpha=.2)
fig.savefig(ROOT/'visual_evidence_reference_vs_collider.png',dpi=170);plt.close(fig)
fig,ax=plt.subplots(figsize=(15,7),constrained_layout=True)
water_ids=[e['from'] for e in water]+[water[-1]['to']]
known=[(i,pd[i]) for i in water_ids if i in pd]
ax.plot(range(len(known)),[-p['mesh_xyz_raw'][1] for _,p in known],'-o',color='#0b7790')
ax.set_xticks(range(len(known)),[i for i,_ in known],rotation=40,ha='right');ax.set_ylabel('relative height = -raw Y (model units)');ax.set_title('Water landmark heights — endpoint evidence only; metric scale and continuous flow unverified');ax.grid(alpha=.2)
fig.savefig(ROOT/'visual_evidence_water_profile.png',dpi=170);plt.close(fig)
result={'schema_version':1,'source_world_model':'existing_Marble_1.1_GLB_SPZ','source_camera_status':cam['status'],'pair_count_reviewed':sum(r['reviewed_pair'] for r in records),'unpaired_ids':[r['id'] for r in records if r['raw_xyz'] is None],'axis':axis,'landmarks':records,'water_edges':water,'navigation_edges':nav,'global_semantic_mask_status':'NOT_CREATED','metric_scale_status':'UNDETERMINED','traversal_status':'UNTESTED','formal_p0b_status':'BLOCKED'}
(ROOT/'registered_spatial_measurements.json').write_text(json.dumps(result,ensure_ascii=False,indent=2))
print('water');[print(e['id'],e['status'],round(e.get('drop_start_to_end_raw_units',float('nan')),4)) for e in water]
print('nav');[print(e['id'],e['status'],round(e.get('endpoint_angle_deg_abs',float('nan')),1)) for e in nav]
print('flags',[(r['id'],r.get('semantic_review_flag')) for r in records if r.get('semantic_review_flag')])

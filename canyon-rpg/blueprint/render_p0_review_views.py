#!/usr/bin/env python3
"""Render source-camera layout overlay and metric top/front/side height review views."""
import json
from pathlib import Path
import numpy as np
import cv2
from PIL import Image
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = ['Arial Unicode MS', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False
ROOT=Path(__file__).resolve().parent
PROJECT=ROOT.parent
ANALYSIS=PROJECT/'analysis/p0_marble_2026-10-26'
blueprint=json.loads((ROOT/'scene_blueprint.json').read_text())
nav=json.loads((ROOT/'navigation_graph.json').read_text())
water=json.loads((ROOT/'water_graph.json').read_text())
source_camera=json.loads((ANALYSIS/'registration/camera_registration_candidate.json').read_text())
reviewed=json.loads((ANALYSIS/'annotations/paired_landmarks_user_reviewed.json').read_text())
landmarks={p['id']:p for p in blueprint['landmarks']}
nav_nodes={p['id']:p for p in nav['nodes']}
water_nodes={p['id']:p for p in water['nodes']}
origin=np.array(blueprint['coordinate_registration']['raw_origin_xyz'],float)
scale=float(blueprint['coordinate_registration']['metric_scale_m_per_raw_unit'])
K=np.array(source_camera['K'],float)
R=np.array(source_camera['rotation_world_to_cv_camera_3x3'],float)
t=np.array(source_camera['translation_world_to_cv_camera'],float)

def design_to_raw(points):
 p=np.asarray(points,float).reshape(-1,3)
 return np.stack([p[:,0]/scale+origin[0],-p[:,1]/scale+origin[1],-p[:,2]/scale+origin[2]],axis=1)

def project_design(points):
 raw=design_to_raw(points)
 cam=(R@raw.T).T+t
 uv=(K@cam.T).T
 return uv[:,:2]/uv[:,2,None],cam[:,2]

# Source image with projected design graph. The PnP camera is a candidate, not a final render.
image=cv2.imread(str(PROJECT/'assets/worlds/canyon-waterfall/canyon-waterfall-reference.jpeg'),cv2.IMREAD_COLOR)
if image is None:raise FileNotFoundError('reference image')
overlay=image.copy()
for domain,edges,nodes,color in [('water',water['edges'],water_nodes,(235,205,17)),('nav',nav['edges'],nav_nodes,(25,151,250))]:
 for edge in edges:
  a=np.array(nodes[edge['from']]['position_m'],float);b=np.array(nodes[edge['to']]['position_m'],float)
  alpha=np.linspace(0,1,30);pts=a[None,:]*(1-alpha[:,None])+b[None,:]*alpha[:,None]
  uv,depth=project_design(pts)
  good=np.isfinite(uv).all(axis=1)&(depth>0)
  for i in range(len(uv)-1):
   if good[i] and good[i+1] and (domain!='water' or edge.get('confidence')!='low' or i%3!=0):
    cv2.line(overlay,tuple(np.rint(uv[i]).astype(int)),tuple(np.rint(uv[i+1]).astype(int)),color,6 if domain=='nav' else 7,cv2.LINE_AA)
result=cv2.addWeighted(image,.55,overlay,.45,0)
errors=[]
for p in reviewed['pairs']:
 if p.get('mesh_xyz_raw') is None:continue
 id=p['id'];uv,_=project_design([landmarks[id]['design_world_xyz_m']]);u,v=np.rint(uv[0]).astype(int);px,py=map(int,p['pixel_xy']);err=float(np.linalg.norm(uv[0]-np.array([px,py])))
 errors.append({'id':id,'error_px':round(err,2),'pixel_xy':[px,py],'projected_xy':[float(uv[0,0]),float(uv[0,1])]})
 cv2.line(result,(px,py),(u,v),(55,55,255),2,cv2.LINE_AA)
 cv2.circle(result,(px,py),7,(255,255,255),2,cv2.LINE_AA)
 cv2.circle(result,(u,v),6,(30,30,255),-1,cv2.LINE_AA)
 if err>50:cv2.putText(result,id,(px+8,py-8),cv2.FONT_HERSHEY_SIMPLEX,.65,(15,15,255),2,cv2.LINE_AA)
cv2.rectangle(result,(20,20),(1000,182),(20,29,34),-1)
cv2.putText(result,'P0 design projected into source camera (candidate)',(35,56),cv2.FONT_HERSHEY_SIMPLEX,.85,(245,245,245),2,cv2.LINE_AA)
cv2.putText(result,'cyan: water  |  orange: designed route  |  white: picked pixel  |  red: projected point',(35,94),cv2.FONT_HERSHEY_SIMPLEX,.63,(235,235,235),2,cv2.LINE_AA)
cv2.putText(result,'Model/image mismatch and hidden surfaces remain; lines are not photo segmentation.',(35,128),cv2.FONT_HERSHEY_SIMPLEX,.56,(200,210,220),1,cv2.LINE_AA)
cv2.putText(result,'PnP median: %.1f px  |  25 reviewed pairs  |  outlet ray not reviewed'%np.median([e['error_px'] for e in errors]),(35,160),cv2.FONT_HERSHEY_SIMPLEX,.57,(200,210,220),1,cv2.LINE_AA)
cv2.imwrite(str(ROOT/'layout_reference_overlay.png'),result)

# Heightfield metric mapping; negative elevations remain valid by documented uint16 offset.
u16=np.array(Image.open(ROOT/'heightmap_16bit.png'),dtype=np.float64)
r=blueprint['raster'];H=r['heightmap_min_m']+u16/65535*(r['heightmap_max_m']-r['heightmap_min_m'])
bounds=blueprint['world_bounds_m'];nx,nz=H.shape[1],H.shape[0]
x=np.linspace(bounds['x_min_m']+(bounds['x_max_m']-bounds['x_min_m'])/(2*nx),bounds['x_max_m']-(bounds['x_max_m']-bounds['x_min_m'])/(2*nx),nx)
z=np.linspace(bounds['z_min_m']+(bounds['z_max_m']-bounds['z_min_m'])/(2*nz),bounds['z_max_m']-(bounds['z_max_m']-bounds['z_min_m'])/(2*nz),nz)
# Front transverse section: x left/right, at main waterfall lip. Side longitudinal section: z upstream/downstream near river.
front_z=-15.5;front_index=int(np.argmin(abs(z-front_z)))
side_x=-2.0;side_index=int(np.argmin(abs(x-side_x)))
fig,axes=plt.subplots(1,3,figsize=(21,7),constrained_layout=True)
ax=axes[0];im=ax.imshow(H,extent=[bounds['x_min_m'],bounds['x_max_m'],bounds['z_max_m'],bounds['z_min_m']],cmap='terrain',vmin=-5,vmax=26)
ax.contour(x,z,H,levels=np.arange(-4,27,4),colors='black',linewidths=.4,alpha=.6)
ax.axhline(front_z,color='crimson',lw=1.4,ls='--');ax.axvline(side_x,color='navy',lw=1.4,ls='--')
for id in ('wf_far','wf_mid','upper_run','pool_main','bridge','stream_lower','left_upper','right_upper'):
 p=landmarks.get(id)
 if p:
  X,Y,Z=p['design_world_xyz_m'];ax.plot(X,Z,'o',ms=3,color='white',mec='black');ax.annotate(id,(X,Z),xytext=(3,3),textcoords='offset points',fontsize=7)
ax.set_title('TOP / 俯视：地形高度等值线');ax.set_xlabel('Godot X / m');ax.set_ylabel('Godot Z / m (上游为负)');ax.set_aspect('equal');fig.colorbar(im,ax=ax,shrink=.65,label='地形 Y / m')
ax=axes[1];profile=H[front_index,:];ax.fill_between(x,-8,profile,color='#c5b992',alpha=.8);ax.plot(x,profile,color='#4e493b',lw=1.7)
for id in ('main_fall_left_rim','main_fall_right_rim','stair_left_upper','right_upper'):
 p=landmarks.get(id)
 if p:
  X,Y,Z=p['design_world_xyz_m'];ax.plot(X,Y,'o',color='#be3119');ax.annotate(id,(X,Y),xytext=(4,4),textcoords='offset points',fontsize=7)
ax.set_title(f'FRONT / 正面切面：Z={z[front_index]:.2f} m');ax.set_xlabel('Godot X / m');ax.set_ylabel('Y / m');ax.set_xlim(-48,48);ax.set_ylim(-8,30);ax.grid(alpha=.25)
ax=axes[2];profile=H[:,side_index];ax.fill_between(z,-8,profile,color='#c5b992',alpha=.8);ax.plot(z,profile,color='#4e493b',lw=1.7)
for id in ('upper_run','main_fall_lip','wf_main','pool_main','bridge_reach','stream_lower'):
 p=water_nodes.get(id)
 if p:
  X,Y,Z=p['position_m'];ax.plot(Z,Y,'o',color='#08a4c5');ax.annotate(id,(Z,Y),xytext=(3,3),textcoords='offset points',fontsize=7)
ax.set_title(f'SIDE / 侧面切面：X={x[side_index]:.2f} m');ax.set_xlabel('Godot Z / m (上游为负)');ax.set_ylabel('Y / m');ax.set_xlim(-85,35);ax.set_ylim(-8,30);ax.grid(alpha=.25)
fig.suptitle('P0 三视图高度核对 | 蓝线/点为设计水面；高度图只含 bulk terrain，桥/阶梯/垂直崖为独立几何',fontsize=13)
fig.savefig(ROOT/'terrain_three_views.png',dpi=180);plt.close(fig)
# Orthographic camera snapshots of the designed heightfield, coarse for visual inspection only.
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401
step=8;Xg,Zg=np.meshgrid(x[::step],z[::step]);Yg=H[::step,::step]
fig=plt.figure(figsize=(18,7),constrained_layout=True)
views=[('TOP / 俯视',90,-90),('FRONT / 下游看上游',0,-90),('SIDE / 右侧看河道',0,0)]
for i,(title,elev,azim) in enumerate(views,1):
 ax=fig.add_subplot(1,3,i,projection='3d',proj_type='ortho')
 ax.plot_surface(Xg,Zg,Yg,rstride=1,cstride=1,cmap='terrain',vmin=-5,vmax=26,linewidth=0,antialiased=False,shade=True)
 ax.view_init(elev=elev,azim=azim);ax.set_title(title,pad=20);ax.set_xlim(-48,48);ax.set_ylim(35,-85);ax.set_zlim(-8,30);ax.set_box_aspect((96,120,38),zoom=1.25);ax.set_axis_off()
fig.suptitle('P0 正交三视角：按高度图生成；不包含桥面、树冠、独立悬崖',fontsize=13)
fig.savefig(ROOT/'terrain_orthographic_views.png',dpi=140);plt.close(fig)
meta={'schema_version':1,'source_camera_status':source_camera['status'],'reprojection_reviewed_pair_count':len(errors),'reprojection_median_px':float(np.median([e['error_px'] for e in errors])),'reprojection_p90_px':float(np.quantile([e['error_px'] for e in errors],.9)),'reprojection_errors':errors,'front_section_z_m':float(z[front_index]),'side_section_x_m':float(x[side_index]),'images':['layout_reference_overlay.png','terrain_three_views.png','terrain_orthographic_views.png'],'limitations':['graph lines are projected from endpoint interpolation, not image segmentation','source PnP camera is a candidate','bulk heightmap excludes bridge, stairs and separate cliff faces']}
(ROOT/'review_views_metadata.json').write_text(json.dumps(meta,ensure_ascii=False,indent=2))
print('Rendered',', '.join(meta['images']),'median',round(meta['reprojection_median_px'],2))

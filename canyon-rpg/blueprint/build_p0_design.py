#!/usr/bin/env python3
"""Build a metric P0 *design* from reviewed Marble anchors, without treating GLB as surveyed terrain.
Outputs Godot Y-up metres, bulk-ground heightfield, topology and masks. No meshes are modeled.
"""
import json, math
from pathlib import Path
import numpy as np
from scipy.interpolate import LinearNDInterpolator, NearestNDInterpolator
from scipy.ndimage import gaussian_filter
from PIL import Image
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
ROOT=Path(__file__).resolve().parent
SRC=ROOT.parent/'analysis/p0_marble_2026-10-26'
P=json.loads((SRC/'annotations/paired_landmarks_user_reviewed.json').read_text())
RAW={p['id']:p for p in P['pairs'] if p.get('mesh_xyz_raw') is not None}
RAYS={p['id']:p for p in json.loads((SRC/'registration/projected_landmarks_unverified.json').read_text())['points']}
BRIDGE_RAW=np.array(RAW['bridge']['mesh_xyz_raw'],float)
BL=np.array(RAW['bridge_left']['mesh_xyz_raw'],float);BR=np.array(RAW['bridge_right']['mesh_xyz_raw'],float)
span_raw=float(np.linalg.norm((BR-BL)[[0,2]]));SCALE=6.0/span_raw
bounds={'x_min_m':-48.0,'x_max_m':48.0,'z_min_m':-85.0,'z_max_m':35.0}
NX,NZ=768,960;dx=(bounds['x_max_m']-bounds['x_min_m'])/NX;dz=(bounds['z_max_m']-bounds['z_min_m'])/NZ
assert abs(dx-dz)<1e-9

def world(raw):
 x,y,z=np.asarray(raw,float);ox,oy,oz=BRIDGE_RAW
 return [round(float((x-ox)*SCALE),4),round(float(-(y-oy)*SCALE),4),round(float(-(z-oz)*SCALE),4)]
W={id:world(p['mesh_xyz_raw']) for id,p in RAW.items()}
# Image-pixel rays for two not-yet-reviewed points are explicit design hypotheses.
exit_ray=RAYS['exit_lower_left']['candidate_hits'][0]['point_raw_xyz'];exit_world=world(exit_ray)
red_ray=RAYS['right_red_tree']['candidate_hits'][0]['point_raw_xyz'];red_world=world(red_ray)
# Use the river slope and viewport exit; do not pretend the unreviewed ray is a user-picked surface.
W['exit_lower_left']=[exit_world[0],round(exit_world[1]-.2,4),exit_world[2]]
W['right_red_tree']=red_world
# Main fall lip takes the midpoint of human-picked left/right rims.
W['main_fall_lip']=[round((W['main_fall_left_rim'][i]+W['main_fall_right_rim'][i])/2,4) for i in range(3)]
# Water centres: endpoints follow reviewed collider heights except proposed exit / lip.
water_ids=['wf_far','wf_mid','upper_run','main_fall_lip','wf_main','pool_main','bridge_reach','stream_lower','exit_lower_left']
water_nodes=[]
for id in water_ids:
 source='reviewed_GLB_anchor' if id in RAW else ('mean_of_reviewed_rim_anchors' if id=='main_fall_lip' else 'unreviewed_source_camera_ray_design_hypothesis')
 water_nodes.append({'id':id,'position_m':W[id],'source':source,'surface_role':'water_surface_or_fall_centerline','walkable':False})
water_edges=[]
edge_types=['distant_cascade','distant_cascade','upper_reach_to_lip','waterfall','waterfall','pool_to_stream','stream','stream_to_exit']
for a,b,kind in zip(water_ids[:-1],water_ids[1:],edge_types):
 dh=round(W[a][1]-W[b][1],4)
 water_edges.append({'id':f'{a}__{b}','from':a,'to':b,'kind':kind,'designed_drop_m':dh,'direction_check':'POSITIVE' if dh>0 else 'FAIL','continuous_collider_surface_proven':False,'water_width_m':4.5 if a=='pool_main' else (2.6 if 'fall' in kind else 2.2),'confidence':'low' if b=='exit_lower_left' else 'medium'})
water={'schema_version':1,'stage':'P0_B_DESIGN','nodes':water_nodes,'edges':water_edges,'hydrology_status':'DESIGN_DIRECTION_VERIFIED_PHYSICAL_FLOW_NOT_SIMULATED','source_camera_not_game_camera':True}
# Route is a designed centerline. Repair known GLB gaps with explicit whitebox stairs or trail surfaces.
main=['start_lower_right','stair_low_right','bridge_right','bridge','bridge_left','left_bank_entry','left_bank_upper','left_glade','stair_left_upper','left_upper']
right=['bridge_right','right_lower','stair_far_right','right_upper']
stair_edges={'left_glade__stair_left_upper','right_lower__stair_far_right','stair_far_right__right_upper'}
bridge_edges={'bridge_right__bridge','bridge__bridge_left'}
nav_edges=[]
for seq,route in [(main,'main'),(right,'right_branch')]:
 for a,b in zip(seq[:-1],seq[1:]):
  id=f'{a}__{b}'
  if any(e['id']==id for e in nav_edges):continue
  p=np.array(W[a]);q=np.array(W[b]);horizontal=float(np.linalg.norm((p-q)[[0,2]]));rise=abs(float(p[1]-q[1]));angle=math.degrees(math.atan2(rise,horizontal))
  kind='bridge' if id in bridge_edges else ('stair' if id in stair_edges else 'path')
  e={'id':id,'from':a,'to':b,'route':route,'kind':kind,'horizontal_length_m':round(horizontal,3),'endpoint_height_delta_m':round(float(q[1]-p[1]),3),'endpoint_slope_deg':round(angle,2),'clear_width_m':1.6 if kind in ('bridge','stair') else 1.8,'construction':'separate_deck' if kind=='bridge' else ('designed_stair_flights' if kind=='stair' else 'graded_path_strip'),'collider_reuse':'DO_NOT_USE_RAW_MARBLE_AS_FINAL_COLLISION'}
  if kind=='stair':
   steps=max(1,math.ceil(rise/.175));riser=rise/steps
   if id=='stair_far_right__right_upper':flights=[22,22,steps-44];landings=2
   else:flights=[steps];landings=0
   e['stairs']={'steps':steps,'flights':flights,'riser_m':round(riser,4),'tread_m':.32,'landing_count':landings,'landing_length_m':1.5,'minimum_run_m':round(steps*.32+landings*1.5,3),'fits_endpoint_horizontal_run':steps*.32+landings*1.5<=horizontal+1e-6}
  nav_edges.append(e)
nav={'schema_version':1,'stage':'P0_B_DESIGN','agent':{'height_m':1.75,'radius_m':.35,'maximum_regular_path_slope_deg':18,'maximum_stair_riser_m':.175,'minimum_overhead_clearance_m':2.1,'godot_navmesh_agent_radius_m':.35,'godot_navmesh_agent_height_m':1.8,'godot_navmesh_agent_max_climb_m':.18,'godot_navmesh_agent_max_slope_deg':35},'nodes':[{'id':id,'position_m':W[id],'source':'reviewed_GLB_anchor','surface':'bridge' if id.startswith('bridge') or id=='bridge' else ('stairs' if id.startswith('stair') else 'terrain_path')} for id in dict.fromkeys(main+right)],'edges':nav_edges,'routes':{'main':main,'right_branch':right},'physical_characterbody_test':'P1_REQUIRED_NOT_RUN','designed_continuity':'GRAPH_AND_DIMENSIONS_VALIDATED_ONLY'}
# Cliff lines are deliberately separate from a single-valued terrain raster.
cliffs={'schema_version':1,'stage':'P0_B_DESIGN','note':'Approximate visible terrain lips; extruded cliff collision and overhangs must be authored separately. Do not convert heightmap slopes into vertical walls.','edges':[
 {'id':'main_fall_lip','polyline_xz_m':[[W['main_fall_left_rim'][0],W['main_fall_left_rim'][2]],[W['main_fall_right_rim'][0],W['main_fall_right_rim'][2]]],'role':'waterfall_lip','confidence':'medium','source_ids':['main_fall_left_rim','main_fall_right_rim']},
 {'id':'left_pool_cliff','polyline_xz_m':[[-25,-9],[-19,-13],[-12,-14],[-7,-11]],'role':'terrace_cliff','confidence':'low','source_ids':['left_glade','left_bank_upper','main_fall_left_rim']},
 {'id':'right_pool_cliff','polyline_xz_m':[[5,-14],[12,-12],[18,-7],[20,3]],'role':'terrace_cliff','confidence':'low','source_ids':['right_upper','right_lower','main_fall_right_rim']},
 {'id':'left_lower_bank','polyline_xz_m':[[-30,12],[-23,8],[-15,5],[-7,3]],'role':'river_bank_rock','confidence':'low','source_ids':['left_lower','stream_lower','bridge_left']}
]}
# Semantic design categories. These are authored intent, not classifier output from GLB.
classes={0:'outside_playable_bounds',1:'bulk_terrain_not_automatically_walkable',2:'riverbed_no_nav',3:'designed_path_strip',4:'bridge_separate_geometry',5:'stairs_separate_geometry',6:'cliff_exclusion',7:'vegetation_exclusion'}
x=np.linspace(bounds['x_min_m']+dx/2,bounds['x_max_m']-dx/2,NX);z=np.linspace(bounds['z_min_m']+dz/2,bounds['z_max_m']-dz/2,NZ);X,Z=np.meshgrid(x,z)
# Ground anchors preserve Marble relative positions; boundary controls are design assumptions.
ground_ids=['bridge_left','bridge_right','left_bank_entry','left_bank_upper','left_glade','stair_left_upper','left_upper','left_lower','start_lower_right','stair_low_right','right_lower','stair_far_right','right_upper','main_fall_left_rim','main_fall_right_rim']
controls=[[W[id][0],W[id][2],W[id][1]] for id in ground_ids]
controls += [[-48,-85,20],[0,-85,25],[48,-85,22],[-48,-45,17],[48,-45,19],[-48,0,12],[48,0,15],[-48,35,2],[0,35,-4],[48,35,4],[-30,-60,18],[25,-60,18],[-30,20,3],[25,20,5]]
# River bed control anchors, including small offset banks to keep the stream nested.
for id in water_ids:
 wx,wy,wz=W[id];depth=1.0 if id=='pool_main' else .7
 controls.append([wx,wz,wy-depth])
 controls.append([wx-3.6,wz,wy+1.4]);controls.append([wx+3.6,wz,wy+1.4])
points=np.array(controls,float);linear=LinearNDInterpolator(points[:,:2],points[:,2],fill_value=np.nan);height=linear(X,Z);miss=np.isnan(height)
if miss.any():height[miss]=NearestNDInterpolator(points[:,:2],points[:,2])(X[miss],Z[miss])
height=gaussian_filter(height,sigma=2.5);height=np.clip(height,-7,28)
mask=np.ones((NZ,NX),dtype=np.uint8);mask[[0,-1],:]=0;mask[:,[0,-1]]=0

def segment_distance(a,b):
 ax,az=a;bx,bz=b;vx=bx-ax;vz=bz-az;t=np.clip(((X-ax)*vx+(Z-az)*vz)/(vx*vx+vz*vz+1e-12),0,1);return np.hypot(X-(ax+t*vx),Z-(az+t*vz)),t
# Carve riverbed from water surface line. Waterfalls stay separate geometry and cliff edges.
for a,b in zip(water_ids[:-1],water_ids[1:]):
 d,t=segment_distance((W[a][0],W[a][2]),(W[b][0],W[b][2]));width=4.8 if a=='pool_main' else 2.8
 surf=W[a][1]*(1-t)+W[b][1]*t;bed=surf-(1.0 if a=='pool_main' else .7)
 core=d<width/2;height[core]=np.minimum(height[core],bed[core]);mask[core]=2
# Path strips are authored surfaces in P1. Heightfield is bulk ground support, not final collision.
for e in nav_edges:
 a,b=e['from'],e['to'];d,_=segment_distance((W[a][0],W[a][2]),(W[b][0],W[b][2]))
 if e['kind']=='bridge':mask[d<e['clear_width_m']/2]=4
 elif e['kind']=='stair':mask[d<e['clear_width_m']/2]=5
 else:mask[d<e['clear_width_m']/2]=3
for e in cliffs['edges']:
 for a,b in zip(e['polyline_xz_m'][:-1],e['polyline_xz_m'][1:]):
  d,_=segment_distance(a,b);mask[d<.6]=6
vegetation=[{'id':'left_pink_bush_zone','center_xz_m':[W['left_pink_bush'][0],W['left_pink_bush'][2]],'radius_m':2.2,'source':'reviewed anchor'},{'id':'right_red_tree_zone','center_xz_m':[red_world[0],red_world[2]],'radius_m':2.8,'source':'unreviewed source-camera ray; design zone only'}]
for v in vegetation:
 cx,cz=v['center_xz_m'];d=np.hypot(X-cx,Z-cz);mask[(d<v['radius_m'])&(mask==1)]=7
# uint16: documented fixed elevation mapping, preserving negative elevations.
hmin,hmax=-8.0,30.0
u16=np.rint((height-hmin)/(hmax-hmin)*65535).clip(0,65535).astype(np.uint16)
Image.fromarray(u16).save(ROOT/'heightmap_16bit.png')
Image.fromarray(mask,mode='L').save(ROOT/'semantic_mask_design.png')
layout={'schema_version':1,'stage':'P0_B_DESIGN','world_id':P['world_id'],'source_assets':{'reference':'assets/worlds/canyon-waterfall/canyon-waterfall-reference.jpeg','collider':'assets/worlds/canyon-waterfall/canyon-waterfall-collider.glb','spz':'assets/worlds/canyon-waterfall/canyon-waterfall-full-res.spz','reviewed_pairs':'analysis/p0_marble_2026-10-26/annotations/paired_landmarks_user_reviewed.json'},'coordinate_registration':{'raw_glb_up':'-Y','display_transform':'shared X rotation 180 degrees for GLB and SPZ','godot_y_up':True,'godot_unit':'1 meter','raw_origin_xyz':BRIDGE_RAW.tolist(),'metric_scale_m_per_raw_unit':SCALE,'scale_type':'AUTHOR_SELECTED_GAME_DESIGN','bridge_span_raw_xz':span_raw,'bridge_span_design_m':6.0,'mapping':'Godot XYZ = scale * (rawX-originX, -(rawY-originY), -(rawZ-originZ))'},'world_bounds_m':bounds,'raster':{'resolution_xz_px':[NX,NZ],'meters_per_pixel':dx,'heightmap':'heightmap_16bit.png','heightmap_min_m':hmin,'heightmap_max_m':hmax,'heightmap_decode':'height_m = min_m + uint16/65535*(max_m-min_m)','semantic_mask':'semantic_mask_design.png','semantic_classes':classes,'heightfield_role':'bulk terrain only; bridges/stairs/cliffs are separate P1 collision geometry','semantic_mask_source':'DESIGN INTENT, not GLB surface classification'},'design_dimensions':{'bridge_span_m':6.0,'bridge_clear_width_m':1.6,'bridge_rail_height_m':1.1,'main_path_clear_width_m':1.8,'side_path_clear_width_m':1.6,'stair_clear_width_m':1.6,'stair_nominal_tread_m':.32,'stair_max_riser_m':.175,'player_height_m':1.75,'player_collision_radius_m':.35},'landmarks':[{'id':id,'kind':p['kind'],'source_pixel_xy':p['pixel_xy'],'raw_glb_xyz':p['mesh_xyz_raw'],'design_world_xyz_m':W[id],'source_confidence':'USER_REVIEWED_PICK','semantic_status':'DESIGN_CLASS_ASSIGNED_FROM_REFERENCE_AND_ROUTE' if id in ground_ids or id in water_ids else 'REFERENCE_LANDMARK_ONLY'} for id,p in RAW.items()]+[{'id':'exit_lower_left','kind':'water_exit','source_pixel_xy':RAYS['exit_lower_left']['pixel_xy'],'raw_glb_xyz':exit_ray,'design_world_xyz_m':W['exit_lower_left'],'source_confidence':'UNREVIEWED_CAMERA_RAY_DESIGN_HYPOTHESIS'}],'vegetation_exclusion_zones':vegetation,'links':{'water_graph':'water_graph.json','navigation_graph':'navigation_graph.json','cliff_edges':'cliff_edges.json','camera':'camera.json'},'uncertainties':['Marble GLB is not surveyed terrain; hidden surfaces and topological connections may be wrong','Source camera high residuals for stream_lower and stair_left_upper','Exit ray is not user-approved 3D point','Semantic mask is a design partition; tree canopy and rock faces in source GLB are not exhaustively classified','Godot CharacterBody3D collision, NavMesh bake and screenshot have not run'], 'phase_gate':'P0_B_DESIGN_COMPLETE_P1_PHYSICS_PENDING'}
# Orthographic game camera: separate from solved source-image perspective camera.
target=np.array([0.,3.,-25.]);offset=np.array([14.,90.,90.]);position=target+offset
camera={'schema_version':1,'camera_type':'orthographic','role':'GAME_CAMERA_NOT_SOURCE_IMAGE_CAMERA','position_m':position.tolist(),'target_m':target.tolist(),'yaw_hint_deg':round(math.degrees(math.atan2(offset[0],offset[2])),2),'pitch_down_deg':round(math.degrees(math.atan2(offset[1],math.hypot(offset[0],offset[2]))),2),'orthographic_size_m':128.0,'aspect_ratio':16/9,'near_m':.1,'far_m':350.0,'projection_review':'NUMERIC_FRUSTUM_CHECK_REQUIRED','source_camera_file':'analysis/p0_marble_2026-10-26/registration/camera_registration_candidate.json'}
for name,obj in [('scene_blueprint.json',layout),('water_graph.json',water),('navigation_graph.json',nav),('cliff_edges.json',cliffs),('camera.json',camera)]:
 (ROOT/name).write_text(json.dumps(obj,ensure_ascii=False,indent=2))
# Visual evidence: actual raster, nodes, routes, and map bounds.
fig,ax=plt.subplots(figsize=(10,12),constrained_layout=True)
ax.imshow(height,extent=[bounds['x_min_m'],bounds['x_max_m'],bounds['z_max_m'],bounds['z_min_m']],cmap='terrain',alpha=.9,vmin=-7,vmax=25)
colors={2:'#30a6c7',3:'#e8bf68',4:'#7f5432',5:'#ded6bd',6:'#777777',7:'#25652f'}
for code,color in colors.items():
 yy,xx=np.where(mask==code)
 if len(xx):ax.scatter(x[xx[::max(1,len(xx)//13000)]],z[yy[::max(1,len(yy)//13000)]],s=1,c=color,alpha=.65,rasterized=True)
for e in water_edges:
 a,b=W[e['from']],W[e['to']];ax.plot([a[0],b[0]],[a[2],b[2]],color='#00d8ff',lw=2)
for e in nav_edges:
 a,b=W[e['from']],W[e['to']];ax.plot([a[0],b[0]],[a[2],b[2]],color='darkorange',lw=2.5 if e['route']=='main' else 1.6)
for id in set(main+right+water_ids):
 p=W[id];ax.plot(p[0],p[2],'.',color='black',ms=4);ax.annotate(id,(p[0],p[2]),xytext=(3,3),textcoords='offset points',fontsize=6,bbox={'facecolor':'white','alpha':.65,'edgecolor':'none','pad':.3})
ax.set_xlim(bounds['x_min_m'],bounds['x_max_m']);ax.set_ylim(bounds['z_max_m'],bounds['z_min_m']);ax.set_aspect('equal');ax.set_xlabel('Godot X (m)');ax.set_ylabel('Godot Z (m), upstream negative');ax.set_title('P0-B design plan — Marble anchored, game-scaled, not surveyed terrain');ax.grid(alpha=.2)
fig.savefig(ROOT/'layout_topdown.png',dpi=180);plt.close(fig)
print(json.dumps({'scale':SCALE,'span_raw':span_raw,'bounds':bounds,'height_minmax':[float(height.min()),float(height.max())],'water_edges':len(water_edges),'nav_edges':len(nav_edges),'out':str(ROOT)},indent=2))

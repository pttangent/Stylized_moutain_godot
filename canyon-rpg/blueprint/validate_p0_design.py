#!/usr/bin/env python3
"""Numerical P0 design checks. Does not impersonate a Godot physics or renderer run."""
import json,math
from pathlib import Path
import numpy as np
from PIL import Image
import networkx as nx
ROOT=Path(__file__).resolve().parent
load=lambda n:json.loads((ROOT/n).read_text())
b=load('scene_blueprint.json');w=load('water_graph.json');n=load('navigation_graph.json');c=load('camera.json');cl=load('cliff_edges.json')
checks=[]
def check(id,ok,detail):checks.append({'id':id,'status':'PASS' if ok else 'FAIL','detail':detail})
h=np.array(Image.open(ROOT/'heightmap_16bit.png'));mask=np.array(Image.open(ROOT/'semantic_mask_design.png'))
check('heightmap_16bit',h.dtype==np.uint16 and h.shape==(960,768),str((h.dtype,h.shape)))
check('semantic_design_mask',mask.dtype==np.uint8 and mask.shape==h.shape and set(np.unique(mask)).issubset(set(map(int,b['raster']['semantic_classes']))),str(np.unique(mask).tolist()))
check('scale_and_bounds',b['coordinate_registration']['metric_scale_m_per_raw_unit']>0 and b['world_bounds_m']['x_max_m']-b['world_bounds_m']['x_min_m']==96 and b['world_bounds_m']['z_max_m']-b['world_bounds_m']['z_min_m']==120,'96 x 120 m; scale from designed 6 m bridge')
check('water_graph_refs',all(e['from'] in {p['id'] for p in w['nodes']} and e['to'] in {p['id'] for p in w['nodes']} for e in w['edges']),'all water references resolve')
check('water_downhill',all(e['designed_drop_m']>0 for e in w['edges']),'all 8 designed water links descend')
wg=nx.DiGraph((e['from'],e['to']) for e in w['edges'])
check('water_single_flow',nx.is_directed_acyclic_graph(wg) and nx.has_path(wg,'wf_far','exit_lower_left'),'one directed source-to-outlet chain')
nd={p['id']:p for p in n['nodes']};ng=nx.Graph((e['from'],e['to']) for e in n['edges'])
check('navigation_graph_refs',all(e['from'] in nd and e['to'] in nd for e in n['edges']),'all route references resolve')
check('main_route_graph_connected',nx.has_path(ng,'start_lower_right','left_upper'),'start to upper left graph path')
check('right_branch_graph_connected',nx.has_path(ng,'bridge','right_upper'),'bridge to upper right graph path')
ordinary=[e for e in n['edges'] if e['kind']=='path']
check('ordinary_path_grades',all(e['endpoint_slope_deg']<=n['agent']['maximum_regular_path_slope_deg'] for e in ordinary),[(e['id'],e['endpoint_slope_deg']) for e in ordinary])
stairs=[e for e in n['edges'] if e['kind']=='stair']
check('stairs_dimensional',len(stairs)==3 and all(e['stairs']['fits_endpoint_horizontal_run'] and .10<=e['stairs']['riser_m']<=.175 and abs(sum(e['stairs']['flights'])-e['stairs']['steps'])==0 for e in stairs),[(e['id'],e['stairs']) for e in stairs])
check('clear_widths',all(e['clear_width_m']>=1.6 and e['clear_width_m']>2*n['agent']['radius_m'] for e in n['edges']),'1.6 m min versus agent diameter .7 m')
# A water surface landmark is beneath bridge deck; actual clearance includes deck thickness later.
wd={p['id']:p for p in w['nodes']};water_y=wd['bridge_reach']['position_m'][1];bridge_y=nd['bridge']['position_m'][1]
check('bridge_water_vertical_separation',bridge_y-water_y>1.0,f'{bridge_y-water_y:.3f} m deck center to water surface before structural thickness')
# All 25 picked anchors must lie inside the authored bounds.
land=[p for p in b['landmarks'] if p['source_confidence']=='USER_REVIEWED_PICK']
lim=b['world_bounds_m'];check('anchors_inside_bounds',len(land)==25 and all(lim['x_min_m']<=p['design_world_xyz_m'][0]<=lim['x_max_m'] and lim['z_min_m']<=p['design_world_xyz_m'][2]<=lim['z_max_m'] for p in land),'25/25 reviewed 3D anchors in bounds')
# Orthographic projection of scene anchors into the game camera frame.
pos=np.array(c['position_m']);target=np.array(c['target_m']);f=(target-pos);f/=np.linalg.norm(f);right=np.cross(f,np.array([0.,1.,0.]));right/=np.linalg.norm(right);up=np.cross(right,f)
vert=c['orthographic_size_m'];horiz=vert*c['aspect_ratio'];project=[]
for p in land:
 d=np.array(p['design_world_xyz_m'])-target;u=float(np.dot(d,right));v=float(np.dot(d,up));project.append((p['id'],u,v))
check('game_camera_anchor_frame',all(abs(u)<=horiz*.47 and abs(v)<=vert*.47 for _,u,v in project),{'horizontal_half_m':horiz/2,'vertical_half_m':vert/2,'extents_uv':[min(u for _,u,_ in project),max(u for _,u,_ in project),min(v for _,_,v in project),max(v for _,_,v in project)]})
check('cliffs_separate',len(cl['edges'])>=3 and b['raster']['heightfield_role'].startswith('bulk terrain'),'cliff/overhangs reserved as separate geometry')
check('source_camera_separate',c['role']=='GAME_CAMERA_NOT_SOURCE_IMAGE_CAMERA' and b['coordinate_registration']['scale_type']=='AUTHOR_SELECTED_GAME_DESIGN','source camera not reused as game camera; scale is a decision')
result={'schema_version':1,'stage':'P0_B_DESIGN_NUMERIC_CHECK','passed':sum(x['status']=='PASS' for x in checks),'failed':sum(x['status']=='FAIL' for x in checks),'checks':checks,'not_tested':['actual CharacterBody3D traversal','Godot NavigationMesh bake','SPZ/GLB synchronized game transform render','GPU screenshot','water physical simulation','terrain vs overhang visual occlusion'],'design_gate':'PASS' if all(x['status']=='PASS' for x in checks) else 'FAIL','engine_runtime_gate':'PENDING_P1'}
(ROOT.parent/'reports/P0_design_validation.json').write_text(json.dumps(result,ensure_ascii=False,indent=2))
print(f"P0 design: {result['passed']} PASS / {result['failed']} FAIL; runtime {result['engine_runtime_gate']}")
for x in checks:
 if x['status']=='FAIL':print('FAIL',x['id'],x['detail'])
raise SystemExit(result['failed']>0)

#!/usr/bin/env python3
"""Projected-XZ triangle intersection survey along proposed graph edges.
This records collision-surface candidates; it does not infer walkability.
"""
import json
from pathlib import Path
import numpy as np
import trimesh
ROOT=Path(__file__).resolve().parent
ASSET=Path(__file__).parents[2]/'assets/worlds/canyon-waterfall/canyon-waterfall-collider.glb'
m=trimesh.load(ASSET,force='mesh')
pairs=json.loads((ROOT/'annotations/paired_landmarks_user_reviewed.json').read_text())['pairs']
pd={p['id']:np.array(p['mesh_xyz_raw'],float) for p in pairs if p.get('mesh_xyz_raw') is not None}
faces=m.triangles.astype(float);norm=m.face_normals;colors=m.visual.vertex_colors[m.faces,:3].mean(axis=1)
# Keep only observed core and potential upward-facing surface; results can still be foliage or water.
cent=faces.mean(axis=1)
base=(cent[:,0]>-2)&(cent[:,0]<2)&(cent[:,2]>.5)&(cent[:,2]<5.5)&(cent[:,1]>-1.5)&(-norm[:,1]>.35)
fidx=np.flatnonzero(base);t=faces[base];n=norm[base];c=colors[base]
x0,z0=t[:,0,0],t[:,0,2];x1,z1=t[:,1,0],t[:,1,2];x2,z2=t[:,2,0],t[:,2,2]
denom=(z1-z2)*(x0-x2)+(x2-x1)*(z0-z2)
validden=np.abs(denom)>1e-10

def hits(x,z):
 bb=(np.minimum(np.minimum(x0,x1),x2)-1e-8<=x)&(np.maximum(np.maximum(x0,x1),x2)+1e-8>=x)&(np.minimum(np.minimum(z0,z1),z2)-1e-8<=z)&(np.maximum(np.maximum(z0,z1),z2)+1e-8>=z)&validden
 ids=np.flatnonzero(bb)
 if not len(ids):return []
 aa=((z1[ids]-z2[ids])*(x-x2[ids])+(x2[ids]-x1[ids])*(z-z2[ids]))/denom[ids]
 bb2=((z2[ids]-z0[ids])*(x-x2[ids])+(x0[ids]-x2[ids])*(z-z2[ids]))/denom[ids]
 cc=1-aa-bb2
 ok=(aa>=-1e-6)&(bb2>=-1e-6)&(cc>=-1e-6)
 ids=ids[ok];aa=aa[ok];bb2=bb2[ok];cc=cc[ok]
 if not len(ids):return []
 ys=aa*t[ids,0,1]+bb2*t[ids,1,1]+cc*t[ids,2,1]
 return [{'face_index':int(fidx[i]),'raw_y':round(float(y),6),'up_normal_dot':round(float(-n[i,1]),3),'rgb':[round(float(v),1) for v in c[i]]} for i,y in zip(ids,ys)]

def survey(file):
 g=json.loads((ROOT/'blueprint'/file).read_text());out=[]
 for e in g['edges']:
  a=pd.get(e['from']);b=pd.get(e['to']);entry={'id':e['id'],'from':e['from'],'to':e['to'],'status':'MISSING_3D_ENDPOINT' if a is None or b is None else 'SURVEYED_NOT_SEMANTICALLY_VERIFIED'}
  if a is not None and b is not None:
   samples=[]
   for alpha in np.linspace(0,1,21):
    pos=a*(1-alpha)+b*alpha;hs=hits(pos[0],pos[2]);hs.sort(key=lambda q:abs(q['raw_y']-pos[1]))
    nearest=hs[0] if hs else None
    samples.append({'t':round(float(alpha),3),'expected_linear_y':round(float(pos[1]),6),'candidate_count':len(hs),'nearest_height_difference_raw_units':round(float(abs(nearest['raw_y']-pos[1])),6) if nearest else None,'nearest_candidate':nearest})
   entry['samples']=samples
   entry['samples_with_any_upward_face']=sum(x['candidate_count']>0 for x in samples)
   entry['samples_with_face_within_0p08_raw_y']=sum(x['nearest_height_difference_raw_units'] is not None and x['nearest_height_difference_raw_units']<=.08 for x in samples)
   entry['max_nearest_height_difference_raw_units']=max((x['nearest_height_difference_raw_units'] for x in samples if x['nearest_height_difference_raw_units'] is not None),default=None)
  out.append(entry)
 return out
res={'schema_version':1,'algorithm':'vertical XZ triangle interpolation, nearest-to-linear-landmark-height candidate','limitations':['no semantic class','no player radius/height','linear expected height may be wrong for real stairs or waterfalls','dense background shell and vegetation can provide false support','no metric scale'], 'navigation':survey('navigation_graph_proposed.json'),'water':survey('water_graph_proposed.json')}
(ROOT/'route_surface_survey.json').write_text(json.dumps(res,ensure_ascii=False,indent=2))
for domain in ('navigation','water'):
 print(domain)
 for e in res[domain]:print(e['id'],e.get('samples_with_any_upward_face'),e.get('samples_with_face_within_0p08_raw_y'),e.get('max_nearest_height_difference_raw_units'))

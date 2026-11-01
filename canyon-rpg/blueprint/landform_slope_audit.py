#!/usr/bin/env python3
"""Art-only multiscale authored heightfield slope diagnostics; no walkability claim."""
import argparse,json
from pathlib import Path
import numpy as np
from PIL import Image
from scipy.ndimage import gaussian_filter

def run(root,out,scales):
 b=json.loads((root/'scene_blueprint.json').read_text())
 r=b['raster']; src=np.asarray(Image.open(root/r['heightmap']))
 if src.ndim!=2 or src.dtype!=np.uint16: raise ValueError('Require single-channel uint16 heightmap')
 step=float(r['meters_per_pixel']); low=float(r['heightmap_min_m']); high=float(r['heightmap_max_m'])
 if step<=0 or high<=low: raise ValueError('Invalid authored heightmap units/range')
 h=low+(src.astype(float)/65535)*(high-low)
 maskfile=root/r.get('semantic_mask','semantic_mask_design.png')
 mask=np.asarray(Image.open(maskfile)) if maskfile.exists() else None
 if mask is not None and mask.shape!=src.shape: raise ValueError('Mask dimension mismatch')
 valid=(mask!=0) if mask is not None else np.ones_like(src,dtype=bool)
 out.mkdir(parents=True,exist_ok=True)
 report={'schema_version':1,'role':'AUTHORED_DESIGN_HEIGHTFIELD_SLOPE_ONLY_NOT_PHYSICAL_GROUND','scales_m':scales,
 'caveats':['Cliffs and waterfalls may be vertical independent meshes','18 degree walking-path advisory is not a global terrain limit','Gaussian diagnostic smoothing does not edit source geometry'],
 'results':{}}
 color=np.array([[50,115,99],[127,172,97],[222,190,87],[226,133,70],[172,81,72],[99,65,86]],dtype=np.uint8)
 for smooth in scales:
  surf=gaussian_filter(h,sigma=smooth/step) if smooth else h
  dz,dx=np.gradient(surf,step,step)
  theta=np.degrees(np.arctan(np.hypot(dx,dz)))
  record={}
  for label,selector in [('all_design',valid),('optional_path_hint',(mask==3) if mask is not None else np.zeros_like(valid))]:
   vals=theta[selector]
   record[label]={'count':int(vals.size),'p50':float(np.percentile(vals,50)) if vals.size else None,
   'p90':float(np.percentile(vals,90)) if vals.size else None,
   'above_18_percent_DIAGNOSTIC_ONLY':float(100*np.mean(vals>18)) if vals.size else None}
  report['results'][str(smooth)]=record
  idx=np.clip(np.digitize(theta,[5,15,30,50,70]),0,5)
  rgba=np.dstack((color[idx],np.where(valid,255,0).astype(np.uint8)))
  Image.fromarray(rgba).save(out/('slope_'+str(smooth).replace('.','p')+'m.png'))
 (out/'slope_audit.json').write_text(json.dumps(report,indent=2))
 print('Art-only slope diagnostic written:',out)
if __name__=='__main__':
 p=argparse.ArgumentParser()
 p.add_argument('--blueprint',type=Path,default=Path(__file__).resolve().parent)
 p.add_argument('--output',type=Path)
 p.add_argument('--scales',type=float,nargs='+',default=[.5,2.,5.])
 a=p.parse_args()
 if any(x<0 or not np.isfinite(x) for x in a.scales): p.error('invalid smoothing scale')
 run(a.blueprint,a.output or a.blueprint.parent/'analysis'/'slope_audit',a.scales)

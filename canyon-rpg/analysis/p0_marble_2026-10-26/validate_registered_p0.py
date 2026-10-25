#!/usr/bin/env python3
"""Validate post-annotation evidence; leave physical and metric gates explicit."""
import json,hashlib
from pathlib import Path
ROOT=Path(__file__).resolve().parent
raw=ROOT/'annotations/paired_landmarks_raw.json';review=ROOT/'annotations/paired_landmarks_user_reviewed.json'
reg=ROOT/'registration/camera_registration_candidate.json';measure=ROOT/'registered_spatial_measurements.json'
rawj=json.loads(raw.read_text());j=json.loads(review.read_text());c=json.loads(reg.read_text());m=json.loads(measure.read_text())
checks=[]
def check(name,ok,evidence):checks.append({'id':name,'status':'PASS' if ok else 'FAIL','evidence':evidence})
rawpairs={p['id']:p for p in rawj['pairs']};reviewpairs={p['id']:p for p in j['pairs']}
check('raw_export_unchanged',hashlib.sha256(raw.read_bytes()).hexdigest()=='692736c4b36510974865c2ceaba2bbd2fe9168ea1cb1565cc7cb2e68c6b26224','SHA-256 of user-exported raw file')
check('all_raw_pairs_preserved',len(rawpairs)==len(reviewpairs)==27 and all(rawpairs[k].get('mesh_xyz_raw')==reviewpairs[k].get('mesh_xyz_raw') and rawpairs[k]['pixel_xy']==reviewpairs[k]['pixel_xy'] for k in rawpairs),'27 pixel records, no coordinate edits')
check('reviewed_complete_pairs',sum(bool(p.get('mesh_xyz_raw')) and p.get('human_approved',False) for p in j['pairs'])==25,'25 complete pairs confirmed by user; 2 remain without 3D')
check('source_camera_ransac',c['inlier_count']>=20 and c['reprojection_median_px']<40,f"{c['inlier_count']}/{c['total_anchor_count']} inliers; median {c['reprojection_median_px']:.2f} px, p90 {c['reprojection_p90_px']:.2f} px")
check('source_camera_rays_hit_mesh',sum(bool(x['candidate_hits']) for x in json.loads((ROOT/'registration/projected_landmarks_unverified.json').read_text())['points'])==27,'27/27 source-image rays intersect GLB, not semantic proof')
water=[e for e in m['water_edges'] if e['status']!='MISSING_3D_ENDPOINT']
check('water_endpoint_direction',len(water)==6 and all(e['drop_start_to_end_raw_units']>0 for e in water),'6/6 measured water links descend under raw -Y up')
check('renderer_axis_consistency',m['axis']['selected_up_axis_raw']=='-Y' and m['axis']['renderer_flip_x_180_makes_raw_minus_y_display_plus_y'],'GLB raw -Y maps to display +Y via shared 180 degree X flip')
check('navigation_endpoints_recorded',sum(e['status']=='ENDPOINTS_ONLY' for e in m['navigation_edges'])==12,'12/12 proposed navigation edge endpoints measured; continuous traversal unresolved')
check('semantic_flags_preserved',sum(bool(p.get('semantic_review_flag')) for p in m['landmarks'])>=5,'5 anchor face color/normal conflicts retained for semantic review')
check('no_unjustified_metric_scale',m['axis']['scale_m_per_raw_unit'] is None,'No bridge/player measurement establishes meters per raw unit')
check('no_false_formal_blueprint',not (ROOT/'blueprint/scene_blueprint.json').exists() and m['formal_p0b_status']=='BLOCKED','Formal Godot P0-B artifact absent')
result={'schema_version':1,'scope':'post_annotation_geometry_and_structural_validation','passed':sum(x['status']=='PASS' for x in checks),'failed':sum(x['status']=='FAIL' for x in checks),'checks':checks,'gate_status':{'camera':'CANDIDATE','relative_up_axis':'EVIDENCE_SUPPORTED','metric_scale':'BLOCKED','semantic_surface_mask':'BLOCKED','continuous_navigation':'BLOCKED','formal_p0b':'BLOCKED'},'upstream_validator_note':'Bundled validate_p0.py reports 35 PASS / 1 FAIL on reviewed draft because no_fabricated_3d hardcodes an unregistered draft. Its stage text also hardcodes no approved pairs. This post-annotation validator does not replace semantic or traversal review.'}
(ROOT/'post_annotation_validation.json').write_text(json.dumps(result,ensure_ascii=False,indent=2))
print(f"Post-annotation: {result['passed']} PASS / {result['failed']} FAIL; P0-B {result['gate_status']['formal_p0b']}")

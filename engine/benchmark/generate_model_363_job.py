import json
from pathlib import Path

src = Path(__file__).with_name('model_363_shapes.json')
out = Path(__file__).with_name('nesting_363_job.generated.json')
definition = json.loads(src.read_text(encoding='utf-8'))
parts = []
order = 0
for shape in definition['shapes']:
    for _ in range(int(shape['count'])):
        parts.append({
            'entity_id': f'shape-{order}',
            'order': order,
            'contour': shape['contour'],
            'holes': shape.get('holes', []),
            'area': float(shape['area']),
            'width': float(shape['width']),
            'height': float(shape['height']),
            'base_rotation_degrees': 0.0,
            'two_sided': False,
            'special_shape': bool(shape['special_shape']),
        })
        order += 1
job = {
    'protocol_version': 2,
    'source': 'nesting.skp-363',
    'optimization_attempts': 56,
    'materials': [{
        'key': 'bt100|17.4',
        'material': 'BT100',
        'thickness': 17.4,
        'group_index': 0,
        'original_part_count': len(parts),
        'configuration': {
            'board_width': 1220.0,
            'board_height': 2440.0,
            'edge_margin': 3.0,
            'cut_gap': 8.0,
            'rotation_divisions': 4,
            'sheet_in_sheet': False,
            'priority_zone_nesting': True,
            'optimize_flip_face': True,
            'compact_directions': ['left', 'bottom'],
            'max_nesting_time_ms': 300000,
        },
        'parts': parts,
    }],
}
out.write_text(json.dumps(job, separators=(',', ':')), encoding='utf-8')
print(out)

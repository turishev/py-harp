from __future__ import annotations # for list annotations
from typing import Mapping, Set
#from typing import TypeAlias
from scale import interval_to_step
from output import format_pitch, format_layouts

from score  import parse_score, get_score_scale
from harmonicas import harmonicas
from harp_utils import HarpScaleLayout, scale_to_layout

def find_harp_for_score(score : str, use_letters=False,
                        harps : str | None = None,
                        drawbend=False, blowbend=False, overblow=False, overdraw=False
                        ):
    '''
    find a suitable harp for a score,
    use_letters : boolean - use note letters instead interval numbers
    '''
    layouts = {}
    harp_list = harmonicas.keys() if harps is None else harps.split(',')
    score_scale = get_score_scale(parse_score(score, use_letters))
    score_scale_steps = [interval_to_step(p) for p in score_scale]

    for harp_name in harp_list:
        harp_layouts : list[HarpScaleLayout] = scale_to_layout(harp_name, score_scale, drawbend, blowbend, overblow, overdraw)
        formatted_layouts = [list(zip(score_scale_steps,
                                 [','.join([format_pitch(p.hole, p.slide, p.method) for p in pitches])
                             for pitches in layout]))
                            for layout in harp_layouts]
        if harp_layouts != []: layouts[harp_name] = formatted_layouts

    return layouts


def find_harp_for_score_print(score : str, use_letters=False,
                        harps : str | None = None,
                        drawbend=False, blowbend=False, overblow=False, overdraw=False
                        ) ->  None:
    print(format_layouts(find_harp_for_score(score, use_letters, harps, drawbend, blowbend, overblow, overdraw)))

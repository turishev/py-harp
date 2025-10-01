from __future__ import annotations # for list annotations
from typing import Mapping, Set
#from typing import TypeAlias
from scale import interval_to_step
from output import format_pitch, format_layouts

from score  import parse_score, get_score_scale
from harmonicas import harmonicas
from harp_utils import HarpScaleLayout, scale_to_layout, get_harp_scale

def _get_layouts_for_scale(score_scale : list[int],
                           harp_name : str,
                           drawbend=False, blowbend=False, overblow=False, overdraw=False
                           ):
    score_scale_steps = [interval_to_step(p) for p in score_scale]
    harp_layouts : list[HarpScaleLayout] = scale_to_layout(harp_name, score_scale, drawbend, blowbend, overblow, overdraw)
    formatted_layouts = [list(zip(score_scale_steps,
                                  [','.join([format_pitch(p.hole, p.slide, p.method) for p in pitches])
                             for pitches in layout]))
                            for layout in harp_layouts]
    return formatted_layouts


def find_harps_for_score(score : str, use_letters=False,
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

    for harp_name in harp_list:
        formatted_layouts = _get_layouts_for_scale(score_scale, harp_name, drawbend, blowbend, overblow, overdraw)
        if formatted_layouts != []: layouts[harp_name] = formatted_layouts

    return layouts


def find_harp_for_score_print(score : str, use_letters=False,
                              harps : str | None = None,
                              drawbend=False, blowbend=False, overblow=False, overdraw=False
                              ) ->  None:
    print(format_layouts(find_harps_for_score(score, use_letters, harps, drawbend, blowbend, overblow, overdraw)))


def harmonica_scale_print(harp_name :  str,
                          drawbend=False, blowbend=False, overblow=False, overdraw=False
                          ) -> None:
    harp = harmonicas[harp_name]
    harp_layout = harp['scale']
    hscale = get_harp_scale(harp_layout, drawbend, blowbend, overblow, overdraw)
    score_scale = [p.interval for p in hscale]
    layouts = {harp_name : _get_layouts_for_scale(score_scale, harp_name, drawbend, blowbend, overblow, overdraw)}
    
    print(format_layouts(layouts))

def harmonica_list_print():
    for harp_name, opts in harmonicas.items():
        print(f"{harp_name} : {opts['description']}")

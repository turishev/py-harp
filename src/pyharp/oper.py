from __future__ import annotations # for list annotations
from typing import Mapping, Union, Optional, TypeAlias, Set

# from dataclasses import dataclass
from itertools import groupby
from operator import attrgetter

from output import ScaleLayout, format_pitch, format_layouts
from score  import parse_score, parse_steps, get_score_scale
from harmonicas import harmonicas
from harp_utils import HarpPitch, HarpScaleLayout, scale_to_layout, get_harp_scale, get_harp_position, get_harp_key
import chords
import scale

ScoreScaleLayout : TypeAlias = list[tuple[int, list[HarpPitch]]] # map scale interval -> list[HarpPitch]

def split_by_field(lst, field_name):
    key_func = attrgetter(field_name)
    sorted_lst = sorted(lst, key=key_func)
    return {k: list(g) for k, g in groupby(sorted_lst, key=key_func)}


def _merge_layouts(layouts):
    layouts_arr_arr = split_by_field(layouts, 'harp_key')
    return {}

def _get_layouts_for_scale(score_scale : list[int],
                           harp_name : str,
                           drawbend=False, blowbend=False, overblow=False, overdraw=False
                           ) -> list[ScoreScaleLayout]:
    '''
    returns: list of lists of tuples, each of which is a pair of score_scale step and harmonica pitch
    '''

    harp_layouts : list[HarpScaleLayout] = scale_to_layout(harp_name, score_scale, drawbend, blowbend, overblow, overdraw)
    print(f"_get_layouts_for_scale harp_layouts:{harp_layouts}\n")
    print(f"harp_layouts:{harp_layouts}\n")
    print(f"score_scale:{score_scale}\n")
    layouts = [list(zip(score_scale, layout)) for layout in harp_layouts]
    return layouts


def _format_scale_layout(layout : ScoreScaleLayout, scale_root : str) -> ScaleLayout:
    # note: we can use any layout element (first) to figure out a position for melody
    scale_first_interval = layout[0][0]
    harp_first_interval = layout[0][1][0].interval
    position = get_harp_position(scale_first_interval, harp_first_interval)

    harp_key = get_harp_key(position, scale_root)
    print(f"_format_scale_layout:{layout}")
    scale_formatted = [
        (
            scale.scale_degree_to_step(pair[0]), # scale interval
            ','.join([format_pitch(p.hole, p.slide, p.method) for p in pair[1]]) # harp hole+method list
        )
        for pair in layout
    ]
    return ScaleLayout(harp_key, position, scale_root, scale_formatted)


def _format_scale_layouts(layouts : list[ScoreScaleLayout], scale_root : str) -> list[ScaleLayout]:
    return sorted([_format_scale_layout(layout, scale_root) for layout in layouts], key=lambda v: v.position)


def _get_layouts_for_scale_formatted(score_scale : list[int], scale_root : str,
                                     harp_name : str,
                                     drawbend=False, blowbend=False, overblow=False, overdraw=False
                                     ) -> list[ScaleLayout]:
    layouts = _get_layouts_for_scale(score_scale, harp_name, drawbend, blowbend, overblow, overdraw)
    return _format_scale_layouts(layouts, scale_root)


def find_harps_for_score(score : str, root : str, use_letters : bool,
                         harp_tuning : Optional[str],
                         harp_key : Optional[str],
                         drawbend : bool, blowbend : bool, overblow : bool, overdraw : bool
                         ) -> Mapping[str, list[ScaleLayout]]:
    '''
    find a suitable harp for a score,
    harps: comma-separated str, is used to limit output list by desirable harmonica types
    use_letters : boolean - use note letters instead interval numbers
    returns: dict which keys are harp-tuning names and values is list of lists of pair of a scale step
    and a harmonica hole-method
    '''
    layouts = {}
    harp_tunnings_list = harmonicas.keys() if harp_tuning is None else harp_tuning.lower().split(',')
    harp_keys_list = [] if harp_key is None else harp_key.lower().split(',')

    if use_letters:
        score_scale_degrees = parse_score(score, root)
    else:
        score_scale_degrees = parse_steps(score)

    score_scale =  get_score_scale(score_scale_degrees)
    # print(score_scale)

    for tuning in harp_tunnings_list:
        formatted_layouts = _get_layouts_for_scale_formatted(score_scale, root, tuning,
                                                             drawbend, blowbend, overblow, overdraw)
        if harp_keys_list != []:
            formatted_layouts = [l for l in formatted_layouts if l.harp_key in harp_keys_list]
        if formatted_layouts != []: layouts[tuning] = formatted_layouts
    # print(layouts)
    return layouts


def find_harp_for_score_print(score : str, root : str, use_letters : bool,
                              harp_tuning : Optional[str],
                              harp_key : Optional[str],
                              drawbend : bool, blowbend : bool, overblow : bool, overdraw : bool
                              ) -> None:
    print(format_layouts(find_harps_for_score(score,
                                              root if root else 'c',
                                              use_letters,
                                              harp_tuning,
                                              harp_key, # None means all harps and all positions
                                              drawbend, blowbend, overblow, overdraw)))


def find_harp_for_arpeggio(score : str, root : str, use_letters : bool,
                           harp_tuning : Optional[str],
                           harp_key : Optional[str],
                           drawbend : bool, blowbend : bool, overblow : bool, overdraw : bool
                           ):
    if use_letters:
        score_scale_degrees = parse_score(score, root)
    else:
        score_scale_degrees = parse_steps(score)

    score_scale =  get_score_scale(score_scale_degrees)
    all_inversions = scale.create_inversions(score_scale)


    layouts = {}
    harp_tunnings_list = harmonicas.keys() if harp_tuning is None else harp_tuning.lower().split(',')
    harp_keys_list = [] if harp_key is None else harp_key.lower().split(',')

    for tuning in harp_tunnings_list:
        layouts_raw = [_get_layouts_for_scale(inv, tuning, drawbend, blowbend, overblow, overdraw)
                       for inv in all_inversions]
        print(f"layouts_raw:{layouts_raw}\n")
        
    return []# TODO
    
    
def _find_harp_for_chord(chord : str,
                         harp_tuning : Optional[str],
                         harp_key : Optional[str],
                         drawbend : bool, blowbend : bool, overblow : bool, overdraw : bool
                         ) -> Mapping[str, list[ScaleLayout]]:
    root,bass,scale = chords.parse_chord(chord) #TODO - return bass also
    scale_str = ','.join(scale)
    return find_harps_for_score(scale_str, root, False,
                                harp_tuning, harp_key,
                                drawbend, blowbend, overblow, overdraw)


def find_harp_for_chord_print(chord : str,
                              harp_tuning : Optional[str],
                              harp_key : Optional[str],
                              drawbend : bool, blowbend : bool, overblow : bool, overdraw : bool
                              ) -> None:
    res = _find_harp_for_chord(chord, harp_tuning, harp_key,
                               drawbend, blowbend, overblow, overdraw)
    print(format_layouts(res))



def harmonica_scale_print(harp_name :  str,
                          drawbend : bool, blowbend : bool, overblow : bool, overdraw : bool
                          ) -> None:
    harp = harmonicas[harp_name]
    harp_layout = harp['scale']
    hscale = get_harp_scale(harp_layout, drawbend, blowbend, overblow, overdraw)
    score_scale = [p.interval for p in hscale]
    layouts = {harp_name : _get_layouts_for_scale_formatted(score_scale, 'c',
                                                            harp_name,
                                                            drawbend, blowbend, overblow, overdraw)}

    print(format_layouts(layouts))

def harmonica_list_print():
    for harp_name, opts in harmonicas.items():
        print(f"{harp_name} : {opts['description']}")

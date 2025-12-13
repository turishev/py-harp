from __future__ import annotations # for list annotations
from typing import Mapping, Union, Optional, TypeAlias, Set

# from dataclasses import dataclass

from scale import interval_to_step
from output import ScaleLayoutFormatted, format_pitch, format_layouts
from score  import parse_score, parse_steps, get_score_scale
from harmonicas import harmonicas
from harp_utils import HarpPitch, HarpScaleLayout, scale_to_layout, get_harp_scale, get_harp_position

ScoreScaleLayout : TypeAlias = list[tuple[int, list[HarpPitch]]] # map scale interval -> list[HarpPitch]


def _get_layouts_for_scale(score_scale : list[int],
                           harp_name : str,
                           drawbend=False, blowbend=False, overblow=False, overdraw=False
                           ) -> list[ScoreScaleLayout]:
    '''
    returns: list of lists of tuples, each of which is a pair of score_scale step and harmonica pitch
    '''

    harp_layouts : list[HarpScaleLayout] = scale_to_layout(harp_name, score_scale, drawbend, blowbend, overblow, overdraw)
    layouts = [list(zip(score_scale, layout)) for layout in harp_layouts]
    return layouts


def _format_scale_layout(layout : ScoreScaleLayout) -> ScaleLayoutFormatted:
    scale_first_interval = layout[0][0]
    harp_first_interval = layout[0][1][0].interval
    harp_key = 'c' #TODO
    position = get_harp_position(scale_first_interval, harp_first_interval)
    scale_fromatted = [
        (
            interval_to_step(pair[0]), # scale interval
            ','.join([format_pitch(p.hole, p.slide, p.method) for p in pair[1]]) # harp hole+method list
        )
        for pair in layout
    ]
    return ScaleLayoutFormatted(harp_key, position, scale_fromatted)


def _format_scale_layouts(layouts : list[ScoreScaleLayout]) -> list[ScaleLayoutFormatted]:
    return sorted([_format_scale_layout(layout) for layout in layouts], key=lambda v: v.position)


def _get_layouts_for_scale_formatted(score_scale : list[int],
                                     harp_name : str,
                                     drawbend=False, blowbend=False, overblow=False, overdraw=False
                                     ) -> list[ScaleLayoutFormatted]:
    layouts = _get_layouts_for_scale(score_scale, harp_name, drawbend, blowbend, overblow, overdraw)
    return _format_scale_layouts(layouts)


def find_harps_for_score(score : str, root : str, use_letters : bool,
                         harps : Optional[str]=None,
                         drawbend=False, blowbend=False, overblow=False, overdraw=False
                         ) -> Mapping[str, list[ScaleLayoutFormatted]]:
    '''
    find a suitable harp for a score,
    harps: comma-separated str, is used to limit output list by desirable harmonica types
    use_letters : boolean - use note letters instead interval numbers
    returns: dict which keys are harp-tuning names and values is list of lists of pair of a scale step
    and a harmonica hole-method
    '''
    layouts = {}
    harp_list = harmonicas.keys() if harps is None else harps.split(',')
    if use_letters:
        score_pitches = parse_score(score, root)
    else:
        score_pitches = parse_steps(score)

    score_scale =  get_score_scale(score_pitches)
    print(score_scale)

    for harp_name in harp_list:
        formatted_layouts = _get_layouts_for_scale_formatted(score_scale,
                                                             harp_name,
                                                             drawbend, blowbend, overblow, overdraw)
        if formatted_layouts != []: layouts[harp_name] = formatted_layouts

    print(layouts)
    return layouts


def find_harp_for_score_print(score : str, root : str, use_letters : bool,
                              harps : Optional[str]=None,
                              drawbend=False, blowbend=False, overblow=False, overdraw=False
                              ) -> None:
    print(format_layouts(find_harps_for_score(score, root, use_letters,
                                              harps,
                                              drawbend, blowbend, overblow, overdraw)))


def harmonica_scale_print(harp_name :  str,
                          drawbend=False, blowbend=False, overblow=False, overdraw=False
                          ) -> None:
    harp = harmonicas[harp_name]
    harp_layout = harp['scale']
    hscale = get_harp_scale(harp_layout, drawbend, blowbend, overblow, overdraw)
    score_scale = [p.interval for p in hscale]
    layouts = {harp_name : _get_layouts_for_scale_formatted(score_scale, harp_name,
                                                            drawbend, blowbend, overblow, overdraw)}

    print(format_layouts(layouts))

def harmonica_list_print():
    for harp_name, opts in harmonicas.items():
        print(f"{harp_name} : {opts['description']}")

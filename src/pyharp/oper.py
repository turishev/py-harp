from __future__ import annotations # for list annotations
from typing import Mapping #, Set
from typing import TypeAlias
from dataclasses import dataclass

from scale import interval_to_step
from output import format_pitch, format_layouts

from score  import parse_score, get_score_scale
from harmonicas import harmonicas
from harp_utils import HarpPitch, HarpScaleLayout, scale_to_layout, get_harp_scale, get_harp_position

ScoreScaleLayout : TypeAlias = list[tuple[int, list[HarpPitch]]] # scale interval -> HarpPitch

@dataclass(frozen=True, slots=True)
class ScaleLayout:
    position : int
    layout : list[tuple[str, str]]


# def _get_layouts_for_scale_formatted(score_scale : list[int],
#                                      harp_name : str,
#                                      drawbend=False, blowbend=False, overblow=False, overdraw=False
#                                      ) -> list[list[tuple[str, str]]]:
#     '''
#     returns: list of lists of tuples, each of which is a pair of
#     scale step str and sound production method str (hole, slide and method)
#     '''
#     score_scale_steps = [interval_to_step(p) for p in score_scale]
#     harp_layouts : list[HarpScaleLayout] = scale_to_layout(harp_name, score_scale, drawbend, blowbend, overblow, overdraw)
#     formatted_layouts = [list(zip(score_scale_steps,
#                                   [','.join([format_pitch(p.hole, p.slide, p.method) for p in pitches])
#                                    for pitches in layout]))
#                             for layout in harp_layouts]
#     return formatted_layouts


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


def _format_scale_layout(layout : ScoreScaleLayout) -> ScaleLayout:
    scale_first_interval = layout[0][0]
    harp_first_interval = layout[0][1][0].interval
    position = get_harp_position(scale_first_interval, harp_first_interval)
    scale_fromatted = [
        (
            interval_to_step(pair[0]), # scale interval
            ','.join([format_pitch(p.hole, p.slide, p.method) for p in pair[1]]) # harp hole+method list
        )
        for pair in layout
    ]
    return ScaleLayout(position, scale_fromatted)


def _format_scale_layouts(layouts : list[ScoreScaleLayout]):
    return sorted([_format_scale_layout(layout) for layout in layouts], key=lambda v: v.position)


def _get_layouts_for_scale_formatted(score_scale : list[int],
                                     harp_name : str,
                                     drawbend=False, blowbend=False, overblow=False, overdraw=False
                                     ):# -> list[list[tuple[str, str]]]:
    layouts = _get_layouts_for_scale(score_scale, harp_name, drawbend, blowbend, overblow, overdraw)
    return _format_scale_layouts(layouts)


def find_harps_for_score(score : str, use_letters=False,
                        harps : str | None = None,
                        drawbend=False, blowbend=False, overblow=False, overdraw=False
                        ) -> Mapping[str, list[list[tuple[str, str]]]]:
    '''
    find a suitable harp for a score,
    harps: comma-separated str, is used to limit output list by desirable harmonica types
    use_letters : boolean - use note letters instead interval numbers
    returns: dict which keys are harp-tuning names and values is list of lists of pair of a scale step and a harmonica hole-method
    '''
    layouts = {}
    harp_list = harmonicas.keys() if harps is None else harps.split(',')
    score_scale = get_score_scale(parse_score(score, use_letters))

    for harp_name in harp_list:
        formatted_layouts = _get_layouts_for_scale_formatted(score_scale, harp_name, drawbend, blowbend, overblow, overdraw)
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
    layouts = {harp_name : _get_layouts_for_scale_formatted(score_scale, harp_name, drawbend, blowbend, overblow, overdraw)}

    print(format_layouts(layouts))

def harmonica_list_print():
    for harp_name, opts in harmonicas.items():
        print(f"{harp_name} : {opts['description']}")

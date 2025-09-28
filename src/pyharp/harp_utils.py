from __future__ import annotations # for list annotations
#from typing import TypeAlias
from dataclasses import dataclass

from score  import parse_note, parse_score, get_score_scale
from harmonicas import Method, harmonicas


@dataclass(frozen=True, slots=True)
class HarpScaleItem:
    interval : int
    hole : int
    method : Method


def get_harp_scale(harp_layout,
                   drawbend=False, blowbend=False, overblow=False, overdraw=False
                   ) -> list[HarpScaleItem]:
    '''
    returns: list[HarpScaleItem]
    sorted by interval, interval started from 0, allowed many items with same interval
    '''

    methods = {Method.DRAW.value, Method.BLOW.value}

    if drawbend:
        methods.add(Method.DRAW_BEND1.value)
        methods.add(Method.DRAW_BEND2.value)
        methods.add(Method.DRAW_BEND3.value)
    if blowbend:
        methods.add(Method.BLOW_BEND1.value)
        methods.add(Method.BLOW_BEND2.value)
    if overblow:
        methods.add(Method.OVERBLOW.value)
    if overdraw:
        methods.add(Method.OVERDRAW.value)

    if harp_layout == []: return []

    scale = [(parse_note(p.pitch).interval, p.hole, p.method)
             for p in harp_layout if p.method.value in methods]
    sorted_scale = sorted(scale, key=lambda v: v[0])
    low_pitch = sorted_scale[0][0]
    return [HarpScaleItem(p[0] - low_pitch, p[1], p[2]) for p in sorted_scale]


def _match_harp_to_score(score_scale : list[int], harp_scale : list[HarpScaleItem]) -> list[list[int]]:
    '''
    match a harp to score
    score_scale : list[int] - score intervals list
    harp_scale : list[HarpScaleItem]
    returns : list[list[int]] - list of suitable scales on the harp
    '''

    hscale = [p.interval for p in harp_scale]
    if hscale == []: return []
    hset = set(hscale)

    low_pitch = min(score_scale)
    result = []

    shift = 0
    while True:
        sscale = [p - low_pitch + shift for p in score_scale]
        shift = shift + 1
        sset = set(sscale)
        if len(sset.difference(hset)) == 0: result.append(sscale)
        if sscale[-1] >= hscale[-1]: break

    return result


def _get_harp_pitch_options(harp_scale : list[HarpScaleItem], pitch : int) -> list[HarpScaleItem]:
    res = [it for it in harp_scale if it.interval == pitch]
    res.sort(key=lambda it: it.method.value)
    return res


def _get_score_layout(score_scale : list[int],
                      harp_scale : list[HarpScaleItem]) -> list[list[list[HarpScaleItem]]]:
    '''
    returns: list[list[list[HarpScaleItem]]] - list of layouts, where each of it list of pitches
    most inner list is a hole+method list of variants for given interval
    '''
    layouts : list[list[int]] = _match_harp_to_score(score_scale, harp_scale)
    return [
        [
            _get_harp_pitch_options(harp_scale, pitch)
            for pitch in layout
        ]
        for layout in layouts
    ]


def _scale_to_layout_for_harp(harp_name : str, score_scale : list[int],
                             drawbend=False, blowbend=False, overblow=False, overdraw=False
                              ) -> list[list[list[HarpScaleItem]]]:
    '''
    returns: list[list[list[HarpScaleItem]]] - list of layouts
    '''
    try:
        harp = harmonicas[harp_name]
        harp_layout = harp['scale']
        hscale = get_harp_scale(harp_layout, drawbend, blowbend, overblow, overdraw)
    except:
        return []

    return _get_score_layout(score_scale, hscale)


def find_harp_for_score(score : str, use_letters=False,
                        harps : str | None = None,
                        drawbend=False, blowbend=False, overblow=False, overdraw=False):
    '''
    find a suitable harp for a score,
    use_letters : boolean - use note letters instead interval numbers
    '''
    result = {}
    harp_list = harmonicas.keys() if harps is None else harps.split(',')
    score_scale = get_score_scale(parse_score(score, use_letters))
    if harp_list == []: return result

    for harp_name in harp_list:
        layout = _scale_to_layout_for_harp(harp_name, score_scale, drawbend, blowbend, overblow, overdraw)
        if layout != []: result[harp_name] = layout

    return result

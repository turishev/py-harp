from __future__ import annotations # for list annotations
from typing import TypeAlias

from dataclasses import dataclass

from scale import scale_degree_to_note
from score  import parse_step, parse_note
from harmonicas import Method, harmonicas


@dataclass(frozen=True, slots=True)
class HarpPitch:
    interval : int
    hole : int
    slide : bool
    method : Method


HarpScaleLayout : TypeAlias = list[list[HarpPitch]]


def get_harp_scale(harp_layout,
                   drawbend=False, blowbend=False, overblow=False, overdraw=False
                   ) -> list[HarpPitch]:
    '''
    returns: list[HarpPitch]
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
        methods.add(Method.BLOW_BEND3.value)
    if overblow:
        methods.add(Method.OVERBLOW.value)
    if overdraw:
        methods.add(Method.OVERDRAW.value)

    if harp_layout == []: return []

    scale = [(parse_step(p.pitch), p.hole, p.slide, p.method)
             for p in harp_layout if p.method.value in methods]

    sorted_scale = sorted(scale, key=lambda v: v[0])
    low_pitch = sorted_scale[0][0]
    return [HarpPitch(p[0] - low_pitch, p[1], p[2], p[3]) for p in sorted_scale]


def _match_harp_to_score(score_scale : list[int], harp_scale : list[HarpPitch]) -> list[list[int]]:
    '''
    match a harp to score
    score_scale : list[int] - score intervals list
    harp_scale : list[HarpPitch]
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


def _get_harp_pitch_options(harp_scale : list[HarpPitch], pitch : int) -> list[HarpPitch]:
    res = [it for it in harp_scale if it.interval == pitch]
    res.sort(key=lambda it: it.method.value)
    return res


def _get_score_layout(score_scale : list[int],
                      harp_scale : list[HarpPitch]) -> list[HarpScaleLayout]:
    '''
    returns: list[HarpScaleLayout] - list of layouts, where each of it list of pitches
    '''
    layouts : list[list[int]] = _match_harp_to_score(score_scale, harp_scale)
    return [
        [
            _get_harp_pitch_options(harp_scale, pitch)
            for pitch in layout
        ]
        for layout in layouts
    ]


def scale_to_layout(harp_name : str, score_scale : list[int],
                    drawbend=False, blowbend=False, overblow=False, overdraw=False
                    ) -> list[HarpScaleLayout]:
    '''
    returns: list[HarpScaleLayout] - list of layouts
    '''
    try:
        harp_layout = harmonicas[harp_name]['scale']
        hscale = get_harp_scale(harp_layout, drawbend, blowbend, overblow, overdraw)
    except Exception as e:
        print(e)
        return []

    return _get_score_layout(score_scale, hscale)


# mapping intervals diff to position number
harp_positions = {
    0 : 1, # c
    7 : 2, # g
    2 : 3, # d
    9 : 4, # a
    4 : 5, # e
    11: 6, # b
    6 : 7, # gb
    1 : 8, # db
    8 : 9, # ab
    3 : 10, # eb
    10 : 11, # bb
    5 : 12, # f
}

circle_of_fifths = ['c', 'g', 'd', 'a', 'e', 'b', 'f#', 'db', 'ab', 'eb', 'bb', 'f']

def get_harp_position(score_interval : int, harp_interval :  int) -> int:
    sintv = score_interval % 12
    hintv = harp_interval % 12
    dintv = hintv - sintv + (0 if hintv >= sintv else 12)
    return harp_positions.get(dintv, 0)


def get_harp_key(position : int, scale_root : str) -> str:
    root_inx = circle_of_fifths.index(scale_root)
    harp_inx = (root_inx - position + 1)
    if harp_inx < 0: harp_inx += 12
    return circle_of_fifths[harp_inx]


def get_scale_note(scale_root : str, step : str) -> str:
    root_interval = parse_note(scale_root)
    step_interval = parse_step(step)
    c_interval = (step_interval + root_interval) % 12

    return scale_degree_to_note(c_interval)

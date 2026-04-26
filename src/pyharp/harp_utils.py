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
    print(f"hset:{hset}\n")
    low_score_scale_degree = score_scale[0]
    low_harp_scale_degree = harp_scale[0].interval

    result = []

    first_scale_steps = set()
    shift = 0
    while True:
        sscale = [p - low_score_scale_degree + shift for p in score_scale]
        print(f"\nsscale:{sscale}")
        if sscale[-1] > hscale[-1]: break

        res_scale = []

        if sscale[0] % 12 not in first_scale_steps: 
            first_scale_steps.add(sscale[0])
            print(f"set:{set(sscale)}")
            if len(set(sscale).difference(hset)) == 0: # layout is found
                res_scale = sscale[:]
                position = get_harp_position(low_score_scale_degree + shift, low_harp_scale_degree)
                print(f"position:{position}")

                # search in upper octaves
                octave = 1
                while True:
                    upper_scale = [v + octave * 12 for v in sscale]
                    up_part = [v for v in upper_scale if v in hset]
                    print(f"upper_scale:{upper_scale} up_part:{up_part}")
                    if len(up_part) > 0: res_scale += up_part
                    if len(up_part) < len(upper_scale): break
                    else: octave += 1

                # add lower part of scale
                lower_scale = [v - 12 for v in sscale]
                print(f"lower_scale:{lower_scale}")
                lo_part = [v for v in lower_scale if v in hset]
                print(f"lo_part:{lo_part}")
                if len(lo_part) > 0:
                    res_scale = lo_part + res_scale
                res_scale.sort()
                print(f"res_scale:{res_scale}")
                result.append(res_scale)
        shift += 1                

    print(f"result:{result}\n")
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



def get_scale_note(scale_root : str, step : str) -> str:
    root_interval = parse_note(scale_root)
    step_interval = parse_step(step)
    c_interval = (step_interval + root_interval) % 12

    return scale_degree_to_note(c_interval)

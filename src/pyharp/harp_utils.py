from __future__ import annotations # for list annotations
# from typing import TypeAlias

from dataclasses import dataclass

from scale import scale_degree_to_note
import score
import harmonicas as hm


@dataclass(frozen=True, slots=True)
class HarpPitch:
    scale_degree : int # root note = 0
    hole : int
    slide : bool
    method : hm.Method


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


def get_harp_position(shift : int) -> int:
    return harp_positions.get(shift % 12, 0)


def get_harp_key(position : int, scale_root : str) -> str:
    root_inx = circle_of_fifths.index(scale_root)
    harp_inx = (root_inx - position + 1)
    if harp_inx < 0: harp_inx += 12
    return circle_of_fifths[harp_inx]


def get_scale_note(scale_root : str, step : str) -> str:
    root_interval = score.parse_note(scale_root)
    step_interval = score.parse_step(step)
    c_interval = (step_interval + root_interval) % 12

    return scale_degree_to_note(c_interval)


def get_harp_scale(harp_layout : list[hm.Pitch],
                   drawbend=False, blowbend=False, overblow=False, overdraw=False
                   ) -> list[HarpPitch]:
    '''
    harp_layout : list[hm.Pitch]
    return: list[HarpPitch], 
    sorted by interval, many items with same interval is allowed
    '''
    methods = {hm.Method.DRAW.value, hm.Method.BLOW.value}

    if drawbend:
        methods.add(hm.Method.DRAW_BEND1.value)
        methods.add(hm.Method.DRAW_BEND2.value)
        methods.add(hm.Method.DRAW_BEND3.value)
    if blowbend:
        methods.add(hm.Method.BLOW_BEND1.value)
        methods.add(hm.Method.BLOW_BEND2.value)
        methods.add(hm.Method.BLOW_BEND3.value)
    if overblow:
        methods.add(hm.Method.OVERBLOW.value)
    if overdraw:
        methods.add(hm.Method.OVERDRAW.value)

    if harp_layout == []: return []

    scale = [HarpPitch(scale_degree=score.parse_step(p.pitch), hole=p.hole, slide=p.slide, method=p.method)
             for p in harp_layout if p.method.value in methods]

    sorted_scale = sorted(scale, key=lambda v: v.scale_degree)
    return sorted_scale

def get_harp_scale_degrees(scale : list[HarpPitch]) -> list[int]:
    '''
    scale : list[HarpPitch]
    return: list[int], list of unique sorted scale degrees 
    '''
    return score.get_score_scale([v.scale_degree for v in scale])

def _match_harp_to_score(score_scale : list[int],
                         harp_scale : list[int],
                         simple_match : bool = False) -> list[tuple[int, list[int]]]:
    '''
    match a harp to score
    score_scale : list[int] - score intervals list
    harp_scale : list[HarpPitch]
    returns : list[tuple[int, list[int]]] - list of tuples
    where first tuple element is a shift scale for matching
    and second is a matching result
    '''

    hset = set(harp_scale)
    # print(f"hset:{hset}\n")
    low_score_scale_degree = score_scale[0]
    low_harp_scale_degree = harp_scale[0]
    result = []
    first_scale_steps = set()
    shift = low_harp_scale_degree - low_score_scale_degree

    while True:
        # print(f"shift:{shift}")
        sscale = [p + shift for p in score_scale]
        # print(f"\nsscale:{sscale}")
        res_set = []

        if sscale[0] % 12 not in first_scale_steps: 
            first_scale_steps.add(sscale[0])
            if len(set(sscale).difference(hset)) == 0: # layout is found
                res_set = set(sscale[:])

                if not simple_match:
                    # search in upper octaves
                    octave = 1
                    while True:
                        upper_scale = [v + octave * 12 for v in sscale]
                        up_part = [v for v in upper_scale if v in hset]
                        # print(f"upper_scale:{upper_scale} up_part:{up_part}")
                        if len(up_part) > 0: res_set.update(up_part)
                        if len(up_part) < len(upper_scale): break
                        else: octave += 1

                    # add lower part of scale
                    lower_scale = [v - 12 for v in sscale]
                    # print(f"lower_scale:{lower_scale}")
                    lo_part = [v for v in lower_scale if v in hset]
                    # print(f"lo_part:{lo_part}")
                    if len(lo_part) > 0:
                        res_set.update(lo_part)

                res_list = list(res_set)
                res_list.sort()
                # print(f"res_scale:{res_list}")
                result.append((shift, res_list))

        if sscale[-1] >= harp_scale[-1]: break
        else: shift += 1
    # print(f"result:{result}\n")
    return result


def _get_harp_pitch_options(harp_scale : list[HarpPitch], scale_degree : int) -> list[HarpPitch]:
    res = [it for it in harp_scale if it.scale_degree == scale_degree]
    res.sort(key=lambda it: it.hole)
    return res


def scale_to_layout(harp_name : str, score_scale : list[int],
                    drawbend=False, blowbend=False, overblow=False, overdraw=False,
                    exactly=False
                    ) -> list[tuple[int, list[tuple[int, list[HarpPitch]]]]]:
    '''
    return: list of pair of  position number and a layout.
    Layout in turn is  list of pair of original scale degree and list of HarpPitch.
    '''
    try:
        harp_layout = hm.known_harmonicas_list[harp_name]['scale']
        full_harp_scale = get_harp_scale(harp_layout, drawbend, blowbend, overblow, overdraw)
        harp_scale = get_harp_scale_degrees(full_harp_scale)
        layouts : list[tuple[int, list[int]]] = _match_harp_to_score(score_scale, harp_scale, exactly)

        return [
            (
                get_harp_position(layout[0]), # harp position
                [(scale_degree - layout[0], # original scale degree (not shifted)
                  _get_harp_pitch_options(full_harp_scale, scale_degree)) for scale_degree in layout[1]] # pitch list
             )
            for layout in layouts
        ]

    except Exception as e:
        print(e)
        return []


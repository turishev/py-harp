from __future__ import annotations # for list annotations
#from typing import TypeAlias
#from collections import namedtuple

from parse_score  import parse_note, parse_score, get_score_scale
from harmonicas import Method, harmonicas


#HarpScaleItem = namedtuple('HarpScaleItem', ['interval', 'hole', 'method'])

def get_harp_scale(harp_layout, drawbend=False, blowbend=False, overblow=False, overdraw=False):
    '''
    returns: list[(interval : int, hole : int, method : Method)]
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
    return sorted_scale if low_pitch == 0 else [(p[0] - low_pitch, p[1], p[2]) for p in sorted_scale]


def _match_harp_to_score(score_scale : list[int], harp_layout) -> list[list[int]]:
    '''
    match a harp to score
    score_scale : list[int] - score intervals list
    harp_scale : list[(int, int, Method)]
    returns : list[list[int]] - list of suitable scales on the harp
    '''

    hscale = [p[0] for p in harp_layout]
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


def _get_harp_pitch_options(harp_scale, pitch : int):
    res = [p for p in harp_scale if p[0] == pitch]
    res.sort(key=lambda v: v[2].value)
    return res


def _get_score_layout(score_scale : list[int], harp_scale):
    '''
    returns: list[(int, Method)] - list of layouts, each list of hole+Method
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
                             drawbend=False, blowbend=False, overblow=False, overdraw=False):
    '''
    returns: list[(int, Method)] - list of layouts, each list of hole+Method
    '''
    try:
        harp = harmonicas[harp_name]
        harp_layout = harp['scale']
        hscale = get_harp_scale(harp_layout, drawbend, blowbend, overblow, overdraw)
    except:
        return []

    return _get_score_layout(score_scale, hscale)


def find_harp_for_score(score : str, score_notes=False,
                        harps : str | None = None,
                        drawbend=False, blowbend=False, overblow=False, overdraw=False):
    '''
    find a suitable harp for a score
    '''
    result = {}
    harp_list = harmonicas.keys() if harps is None else harps.split(',')
    score_scale = get_score_scale(parse_score(score, score_notes))
    if harp_list == []: return result

    for harp_name in harp_list:
        layout = _scale_to_layout_for_harp(harp_name, score_scale, drawbend, blowbend, overblow, overdraw)
        if layout != []: result[harp_name] = layout

    return result

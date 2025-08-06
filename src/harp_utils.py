from typing import TypeAlias

from parse_score  import ScorePitch, score_to_scale_intervals, score_steps_to_scale, parse_note, parse_score, get_score_scale_intervals, score_to_scale
from harmonicas import Method, harmonicas


def get_harp_scale(harp_name : str,
                   drawbend=False, blowbend=False, overblow=False, overdraw=False
                   ):
    '''
    returns: (interval, hole, method)
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

    harp = harmonicas[harp_name]

    orig_scale = harp['scale']
    scale = [p for p in orig_scale if p.method.value in methods]

    return [(parse_note(p.pitch).interval, p.hole, p.method) for p in scale]



def get_harp_scale_intervals(harp_name : str,
                   drawbend=False, blowbend=False, overblow=False, overdraw=False
                   ) -> list[int]:
    '''
    returns: sorted list of intervals started from 0
    '''
    pitches = [p[0] for p in get_harp_scale(harp_name, drawbend, blowbend, overblow, overdraw)]

    return score_steps_to_scale(pitches)


def match_harp_to_score(score_scale : list[int], harp_name : str,
                        drawbend=False, blowbend=False, overblow=False, overdraw=False
                        ) -> list[list[int]]:
    '''
    match a harp to score
    score : intervals list
    score_notes : boolean - use letters or steps nums
    returns : list of scale lists
    '''

    hscale = get_harp_scale_intervals(harp_name, drawbend, blowbend, overblow, overdraw)

    hset = set(hscale)
    min_intr = min(score_scale)
    result = []

    for i in range(max(hscale) - max(score_scale)):
        sscale = [p - min_intr + i for p in score_scale]
        #print(f'sscale={sscale}')
        sset = set(sscale)
        if len(sset.difference(hset)) == 0: result.append(sscale)
    return result



# def find_harp_for_score(score : str, score_notes=False):
#     '''find a suitable harp for a score'''
#     score_scale = score_to_scale(parse_score(score, score_notes))
#     for name,data in harmonicas.items():
#         print(name)
#         print(data['scale'])

#     return None # TODO

def print_scale_layout_for_harp(harp_name : str, scale : list[int]) -> None:
    print('Harmonica type: ' + harp_name)

def scale_to_layout_for_harp(harp_name : str, score_scale : list[int],
                             drawbend=False, blowbend=False, overblow=False, overdraw=False):
    '''
    returns: list of layouts, each list of hole+Method
    '''
    hscale = get_harp_scale(harp_name, drawbend, blowbend, overblow, overdraw)
    print(hscale)
    matched_scales = match_harp_to_score(score_scale, harp_name)
    print(matched_scales)
    return list(map(lambda scale: list(map(lambda pitch: list(filter(lambda p: p[0] == pitch,
                                                                     hscale)),
                                           scale)),
                    matched_scales))

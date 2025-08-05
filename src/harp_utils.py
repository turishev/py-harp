from parse_score  import score_to_scale_intervals, parse_note, parse_score, get_score_scale_intervals
from harmonicas import Method, harmonicas


def get_harp_scale(harp, drawbend=False, blowbend=False, overblow=False, overdraw=False):
    '''
    harp : dict {'scale': [Pitch]}
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

    orig_scale = harp['scale']
    scale = [p for p in orig_scale if p.method.value in methods]
    pitches = [parse_note(p.pitch) for p in scale]

    return score_to_scale_intervals(pitches)


def match_harp_to_score(score, harp_name, drawbend=False, blowbend=False, overblow=False, overdraw=False):
    '''
    match a harp to score
    score : [int] - intervals list
    score_notes : boolean - use letters or steps nums
    '''
    harp = harmonicas[harp_name]
    hscale = get_harp_scale(harp, drawbend, blowbend, overblow, overdraw)
    hscale_len = len(hscale)
    score_len = len(score)
    print(f'score:{score}')
    print(f'harp:{hscale}')
    if score_len > hscale_len: return None
    for i in range(hscale_len - score_len):
        print(hscale[i:i+score_len])
    return None
    


def find_harp_for_score(score, score_notes=False):
    '''
    find a suitable harp for a score
    score : string
    '''
    score_scale = get_score_scale_intervals(score, score_notes)
    return None # TODO

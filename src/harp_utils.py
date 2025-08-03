from parse_score  import score_to_scale_intervals, parse_note
from harmonicas import Method


def harp_scale(harp, drawbend=False, blowbend=False, overblow=False, overdraw=False):
    methods = {Method.DRAW, Method.BLOW}
    if drawbend:
        methods.add(Method.DRAW_BEND1)
        methods.add(Method.DRAW_BEND2)
        methods.add(Method.DRAW_BEND3)
    if blowbend:
        methods.add(Method.BLOW_BEND1)
        methods.add(Method.BLOW_BEND2)
    if overblow:
        methods.add(Method.OVERBLOW)
    if overdraw:
        methods.add(Method.OVERDRAW)
    print(methods)

    orig_scale = harp['scale']
    print(orig_scale)
    print(orig_scale[0].method)
    print(orig_scale[0].method.value == Method.BLOW.value)
    print(orig_scale[0].method.value in {Method.BLOW.value})
    #scale = [p for p in orig_scale if p.method in methods]
    scale = [p for p in orig_scale if p.method in {Method.DRAW}]

    print(scale)
    pitches = [parse_note(p.pitch) for p in scale]

    return score_to_scale_intervals(pitches)



from harmonicas import Method

def format_pitch(hole, method):
    '''
    +1o - - overblow
    -8o - overdraw
    -3b -3bb -3bbb - bends
    -2s +2s +2sb - slide (add it later)
    '''
    blow = [Method.BLOW, Method.OVERBLOW, Method.BLOW_BEND1, Method.BLOW_BEND2]
    draw = [Method.DRAW, Method.DRAW_BEND1, Method.DRAW_BEND2, Method.DRAW_BEND3, Method.OVERDRAW]

    method_mark = {
        Method.BLOW : '',
        Method.OVERBLOW : 'o',
        Method.BLOW_BEND1 : 'b',
        Method.BLOW_BEND2 : 'bb',
        Method.DRAW : '',
        Method.DRAW_BEND1 : 'b',
        Method.DRAW_BEND2 : 'bb',
        Method.DRAW_BEND3 : 'bbb',
        Method.OVERDRAW : 'o'
    }

    if method in blow: in_out = '+'
    elif method in draw: in_out = '-'
    else: in_out = ''
    
    return in_out + str(hole) + method_mark.get(method, '')


def scale_layout_str(score_scale, harp_layouts):
    # for layout in layouts:
    #     for pitch_opts in layout:
    #         for pitch in pitch_opts:
    #             s = format_pitch(pitch[1], pitch[2])

    # list(map(lambda layout: list(map(lambda pitch_opts:
    #                                  , layout)),
    #          layouts))

    

from harmonicas import Method

def format_pitch(hole : int, method : Method) -> str:
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


    

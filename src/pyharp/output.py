from harmonicas import Method
from dataclasses import dataclass
from typing import Mapping
from harp_utils import get_scale_note

@dataclass(frozen=True, slots=True)
class ScaleLayoutFormatted:
    harp_key : str
    position : int
    scale_root : str
    layout : list[tuple[str, str]]

def format_pitch(hole : int, slide : bool, method : Method) -> str:
    '''
    +1o - - overblow
    -8o - overdraw
    -3b -3bb -3bbb - bends
    -2s +2s +2sb - slide (add it later)
    '''
    blow = [Method.BLOW, Method.OVERBLOW, Method.BLOW_BEND1, Method.BLOW_BEND2]
    draw = [Method.DRAW, Method.DRAW_BEND1, Method.DRAW_BEND2, Method.DRAW_BEND3, Method.OVERDRAW]

    slide_mark = 's' if slide else ''

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

    return in_out + str(hole) + slide_mark + method_mark.get(method, '')


def format_layouts(harp_layouts : Mapping[str, list[ScaleLayoutFormatted]]) -> str:
    result = ""
    layout_frmt = "harp {key} {pos}pos  {layout}"
    pitch_frmt = "{step}({note}):{method}"

    for scale_name,layouts in harp_layouts.items():
        result = result + f"Harp tuning: {scale_name}\n"
        layouts_str = "\n".join([layout_frmt.format(key=l.harp_key.capitalize(),
                                                    pos=str(l.position),
                                                    layout="  ".join([pitch_frmt.format(step=p[0],
                                                                                        note=get_scale_note(l.scale_root, p[0]).capitalize(),
                                                                                        method=p[1])
                                               for p in l.layout]))
                                 for l in layouts])
        result = result + str(layouts_str) + "\n"
    return result

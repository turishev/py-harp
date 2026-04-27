import pytest

from harmonicas import Method
from harp_utils import HarpPitch
from output import ScaleLayout
from oper import _format_scale_layout

def test_format_scale_layout():
    ## result of scale_to_layout('richter', [0,4,7]) for position=2 
    layout = [
        (-5, [HarpPitch(2, 1, False, Method.DRAW)]),
        (0, [HarpPitch(7, 2, False, Method.DRAW),
             HarpPitch(7, 3, False, Method.BLOW)]),
        (4, [HarpPitch(11, 3, False, Method.DRAW)]),
        (7, [HarpPitch(14, 4, False, Method.DRAW)]),
        (12, [HarpPitch(19, 6, False, Method.BLOW)]),
        (16, [HarpPitch(23, 7, False, Method.DRAW)]),
        (19, [HarpPitch(26, 8, False, Method.DRAW)]),
        (24, [HarpPitch(31, 9, False, Method.BLOW)]),
    ]

    assert _format_scale_layout(2, 'c', layout) == ScaleLayout(
        harp_key='f', 
        position=2, 
        scale_root='c', 
        layout=[
            ('5/0', '-1'), 
            ('1', '-2,+3'), 
            ('3', '-3'), 
            ('5', '-4'), 
            ('1/2', '+6'), 
            ('3/2', '-7'), 
            ('5/2', '-8'), 
            ('1/3', '+9')
        ])

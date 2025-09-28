import pytest
from harmonicas import Pitch
from harp_utils import  HarpPitch,_match_harp_to_score, _get_score_layout, get_harp_scale
from harmonicas import Method

richter_full_scale = [
    HarpPitch(0, 1, Method.BLOW),
    HarpPitch(1, 1, Method.DRAW_BEND1),
    HarpPitch(2, 1, Method.DRAW),
    HarpPitch(3, 1, Method.OVERBLOW),
    HarpPitch(4, 2, Method.BLOW),
    HarpPitch(5, 2, Method.DRAW_BEND2),
    HarpPitch(7, 2, Method.DRAW),
    HarpPitch(7, 3, Method.BLOW),
    HarpPitch(8, 3, Method.DRAW_BEND3),
    HarpPitch(9, 3, Method.DRAW_BEND2),
    HarpPitch(10, 3, Method.DRAW_BEND1),
    HarpPitch(11, 3, Method.DRAW),
    HarpPitch(12, 4, Method.BLOW),
    HarpPitch(13, 4, Method.DRAW_BEND1),
    HarpPitch(14, 4, Method.DRAW),
    HarpPitch(15, 4, Method.OVERBLOW),
    HarpPitch(16, 5, Method.BLOW),
    HarpPitch(17, 5, Method.DRAW),
    HarpPitch(18, 5, Method.OVERBLOW),
    HarpPitch(19, 6, Method.BLOW),
    HarpPitch(20, 6, Method.DRAW_BEND1),
    HarpPitch(21, 6, Method.DRAW),
    HarpPitch(22, 6, Method.OVERBLOW),
    HarpPitch(23, 7, Method.DRAW),
    HarpPitch(24, 7, Method.BLOW),
    HarpPitch(26, 8, Method.DRAW),
    HarpPitch(27, 8, Method.BLOW_BEND1),
    HarpPitch(28, 8, Method.BLOW),
    HarpPitch(29, 9, Method.DRAW),
    HarpPitch(30, 9, Method.BLOW_BEND1),
    HarpPitch(31, 9, Method.BLOW),
    HarpPitch(32, 9, Method.OVERDRAW),
    HarpPitch(33, 10, Method.DRAW),
    HarpPitch(34, 10, Method.BLOW_BEND2),
    HarpPitch(35, 10, Method.BLOW_BEND1),
    HarpPitch(36, 10, Method.BLOW),
    HarpPitch(37, 10, Method.OVERDRAW)
]


richter_diatonic_scale = [
    HarpPitch(0, 1, Method.BLOW),
    HarpPitch(2, 1, Method.DRAW),
    HarpPitch(4, 2, Method.BLOW),
    HarpPitch(7, 2, Method.DRAW),
    HarpPitch(7, 3, Method.BLOW),
    HarpPitch(11, 3, Method.DRAW),
    HarpPitch(12, 4, Method.BLOW),
    HarpPitch(14, 4, Method.DRAW),
    HarpPitch(16, 5, Method.BLOW),
    HarpPitch(17, 5, Method.DRAW),
    HarpPitch(19, 6, Method.BLOW),
    HarpPitch(21, 6, Method.DRAW),
    HarpPitch(23, 7, Method.DRAW),
    HarpPitch(24, 7, Method.BLOW),
    HarpPitch(26, 8, Method.DRAW),
    HarpPitch(28, 8, Method.BLOW),
    HarpPitch(29, 9, Method.DRAW),
    HarpPitch(31, 9, Method.BLOW),
    HarpPitch(33, 10, Method.DRAW),
    HarpPitch(36, 10, Method.BLOW),
]


def test_get_harp_scale():
    harp_scale = [# part of richer scale
            Pitch(10, '6/3', Method.DRAW),
            Pitch(10, '7b/3', Method.BLOW_BEND2),
            Pitch(10, '7/3', Method.BLOW_BEND1),
            Pitch(10, '1/4', Method.BLOW),
            Pitch(10, '2b/4', Method.OVERDRAW),

            Pitch(2, '3/1', Method.BLOW),
            Pitch(2, '4/1', Method.DRAW_BEND2),
            Pitch(2, '4b/1', Method.DRAW_BEND1),
            Pitch(2, '5/1', Method.DRAW),

            Pitch(3, '5/1', Method.BLOW),
            Pitch(3, '6b/1', Method.DRAW_BEND3),
            Pitch(3, '6/1', Method.DRAW_BEND2),
            Pitch(3, '7b/1', Method.DRAW_BEND1),
            Pitch(3, '7/1', Method.DRAW),

            Pitch(6, '7b/2', Method.OVERBLOW),
    ]

    assert get_harp_scale(harp_scale) == [
        HarpPitch(0, 2, Method.BLOW),
        HarpPitch(3, 2, Method.DRAW),
        HarpPitch(3, 3, Method.BLOW),
        HarpPitch(7, 3, Method.DRAW),
        HarpPitch(29, 10, Method.DRAW),
        HarpPitch(32, 10, Method.BLOW),
    ]

    assert get_harp_scale(harp_scale, drawbend=True) == [
        HarpPitch(0, 2, Method.BLOW),
        HarpPitch(0, 2, Method.DRAW_BEND1),
        HarpPitch(1, 2, Method.DRAW_BEND2),
        HarpPitch(3, 2, Method.DRAW),
        HarpPitch(3, 3, Method.BLOW),
        HarpPitch(4, 3, Method.DRAW_BEND3),
        HarpPitch(5, 3, Method.DRAW_BEND2),
        HarpPitch(6, 3, Method.DRAW_BEND1),
        HarpPitch(7, 3, Method.DRAW),
        HarpPitch(29, 10, Method.DRAW),
        HarpPitch(32, 10, Method.BLOW),
    ]

    assert get_harp_scale(harp_scale, blowbend=True) == [
        HarpPitch(0, 2, Method.BLOW),
        HarpPitch(3, 2, Method.DRAW),
        HarpPitch(3, 3, Method.BLOW),
        HarpPitch(7, 3, Method.DRAW),
        HarpPitch(29, 10, Method.DRAW),
        HarpPitch(30, 10, Method.BLOW_BEND2),
        HarpPitch(31, 10, Method.BLOW_BEND1),
        HarpPitch(32, 10, Method.BLOW),
    ]

    assert get_harp_scale(harp_scale, overblow=True) == [
        HarpPitch(0, 2, Method.BLOW),
        HarpPitch(3, 2, Method.DRAW),
        HarpPitch(3, 3, Method.BLOW),
        HarpPitch(7, 3, Method.DRAW),
        HarpPitch(18, 6, Method.OVERBLOW),
        HarpPitch(29, 10, Method.DRAW),
        HarpPitch(32, 10, Method.BLOW),
    ]

    assert get_harp_scale(harp_scale, overdraw=True) == [
        HarpPitch(0, 2, Method.BLOW),
        HarpPitch(3, 2, Method.DRAW),
        HarpPitch(3, 3, Method.BLOW),
        HarpPitch(7, 3, Method.DRAW),
        HarpPitch(29, 10, Method.DRAW),
        HarpPitch(32, 10, Method.BLOW),
        HarpPitch(33, 10, Method.OVERDRAW),
    ]



def test_match_harp_to_score():
    assert _match_harp_to_score([1,3,5], richter_full_scale) == [
        [0, 2, 4],
        [1, 3, 5],
        [3, 5, 7],
        [5, 7, 9],
        [7, 9, 11],
        [8, 10, 12],
        [9, 11, 13],
        [10, 12, 14],
        [11, 13, 15],
        [12, 14, 16],
        [13, 15, 17],
        [14, 16, 18],
        [15, 17, 19],
        [16, 18, 20],
        [17, 19, 21],
        [18, 20, 22],
        [19, 21, 23],
        [20, 22, 24],
        [22, 24, 26],
        [24, 26, 28],
        [26, 28, 30],
        [27, 29, 31],
        [28, 30, 32],
        [29, 31, 33],
        [30, 32, 34],
        [31, 33, 35],
        [32, 34, 36],
        [33, 35, 37],
    ]

def test_get_score_layout():
    assert _get_score_layout([0,36], richter_diatonic_scale) == [
        [[HarpPitch(0, 1, Method.BLOW)], [HarpPitch(36, 10, Method.BLOW)]],
    ]

    assert _get_score_layout([0,7,36], richter_diatonic_scale) == [
       [
           [HarpPitch(0, 1, Method.BLOW)],
           [HarpPitch(7, 3, Method.BLOW), HarpPitch(7, 2, Method.DRAW)], # 2 options for the pitch
           [HarpPitch(36, 10, Method.BLOW)],
       ],
    ]

    assert _get_score_layout([1,8,37], richter_diatonic_scale) == [
       [
           [HarpPitch(0, 1, Method.BLOW)],
           [HarpPitch(7, 3, Method.BLOW), HarpPitch(7, 2, Method.DRAW)], # 2 options for the pitch
           [HarpPitch(36, 10, Method.BLOW)],
       ],
    ]

    assert _get_score_layout([1,3,5], richter_diatonic_scale) == [
       [
           [HarpPitch(0, 1, Method.BLOW,),],
           [HarpPitch(2, 1, Method.DRAW,),],
           [HarpPitch(4, 2, Method.BLOW,),],
       ],
       [
           [HarpPitch(12, 4, Method.BLOW,),],
           [HarpPitch(14, 4, Method.DRAW,),],
           [HarpPitch(16, 5, Method.BLOW,),],
       ],
       [
           [HarpPitch(17, 5, Method.DRAW,),],
           [HarpPitch(19, 6, Method.BLOW,),],
           [HarpPitch(21, 6, Method.DRAW,),],
       ],
       [
           [HarpPitch(19, 6, Method.BLOW,),],
           [HarpPitch(21, 6, Method.DRAW,),],
           [HarpPitch(23, 7, Method.DRAW,),],
       ],
       [
           [HarpPitch(24, 7, Method.BLOW,),],
           [HarpPitch(26, 8, Method.DRAW,),],
           [HarpPitch(28, 8, Method.BLOW,),],
       ],
       [
           [HarpPitch(29, 9, Method.DRAW,),],
           [HarpPitch(31, 9, Method.BLOW,),],
           [HarpPitch(33, 10, Method.DRAW,),],
       ],
   ]

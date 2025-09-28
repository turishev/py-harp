import pytest
from harmonicas import Pitch
from harp_utils import  HarpScaleItem,_match_harp_to_score, _get_score_layout, get_harp_scale
from harmonicas import Method

richter_full_scale = [
    HarpScaleItem(0, 1, Method.BLOW),
    HarpScaleItem(1, 1, Method.DRAW_BEND1),
    HarpScaleItem(2, 1, Method.DRAW),
    HarpScaleItem(3, 1, Method.OVERBLOW),
    HarpScaleItem(4, 2, Method.BLOW),
    HarpScaleItem(5, 2, Method.DRAW_BEND2),
    HarpScaleItem(7, 2, Method.DRAW),
    HarpScaleItem(7, 3, Method.BLOW),
    HarpScaleItem(8, 3, Method.DRAW_BEND3),
    HarpScaleItem(9, 3, Method.DRAW_BEND2),
    HarpScaleItem(10, 3, Method.DRAW_BEND1),
    HarpScaleItem(11, 3, Method.DRAW),
    HarpScaleItem(12, 4, Method.BLOW),
    HarpScaleItem(13, 4, Method.DRAW_BEND1),
    HarpScaleItem(14, 4, Method.DRAW),
    HarpScaleItem(15, 4, Method.OVERBLOW),
    HarpScaleItem(16, 5, Method.BLOW),
    HarpScaleItem(17, 5, Method.DRAW),
    HarpScaleItem(18, 5, Method.OVERBLOW),
    HarpScaleItem(19, 6, Method.BLOW),
    HarpScaleItem(20, 6, Method.DRAW_BEND1),
    HarpScaleItem(21, 6, Method.DRAW),
    HarpScaleItem(22, 6, Method.OVERBLOW),
    HarpScaleItem(23, 7, Method.DRAW),
    HarpScaleItem(24, 7, Method.BLOW),
    HarpScaleItem(26, 8, Method.DRAW),
    HarpScaleItem(27, 8, Method.BLOW_BEND1),
    HarpScaleItem(28, 8, Method.BLOW),
    HarpScaleItem(29, 9, Method.DRAW),
    HarpScaleItem(30, 9, Method.BLOW_BEND1),
    HarpScaleItem(31, 9, Method.BLOW),
    HarpScaleItem(32, 9, Method.OVERDRAW),
    HarpScaleItem(33, 10, Method.DRAW),
    HarpScaleItem(34, 10, Method.BLOW_BEND2),
    HarpScaleItem(35, 10, Method.BLOW_BEND1),
    HarpScaleItem(36, 10, Method.BLOW),
    HarpScaleItem(37, 10, Method.OVERDRAW)
]


richter_diatonic_scale = [
    HarpScaleItem(0, 1, Method.BLOW),
    HarpScaleItem(2, 1, Method.DRAW),
    HarpScaleItem(4, 2, Method.BLOW),
    HarpScaleItem(7, 2, Method.DRAW),
    HarpScaleItem(7, 3, Method.BLOW),
    HarpScaleItem(11, 3, Method.DRAW),
    HarpScaleItem(12, 4, Method.BLOW),
    HarpScaleItem(14, 4, Method.DRAW),
    HarpScaleItem(16, 5, Method.BLOW),
    HarpScaleItem(17, 5, Method.DRAW),
    HarpScaleItem(19, 6, Method.BLOW),
    HarpScaleItem(21, 6, Method.DRAW),
    HarpScaleItem(23, 7, Method.DRAW),
    HarpScaleItem(24, 7, Method.BLOW),
    HarpScaleItem(26, 8, Method.DRAW),
    HarpScaleItem(28, 8, Method.BLOW),
    HarpScaleItem(29, 9, Method.DRAW),
    HarpScaleItem(31, 9, Method.BLOW),
    HarpScaleItem(33, 10, Method.DRAW),
    HarpScaleItem(36, 10, Method.BLOW),
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
        HarpScaleItem(0, 2, Method.BLOW),
        HarpScaleItem(3, 2, Method.DRAW),
        HarpScaleItem(3, 3, Method.BLOW),
        HarpScaleItem(7, 3, Method.DRAW),
        HarpScaleItem(29, 10, Method.DRAW),
        HarpScaleItem(32, 10, Method.BLOW),
    ]

    assert get_harp_scale(harp_scale, drawbend=True) == [
        HarpScaleItem(0, 2, Method.BLOW),
        HarpScaleItem(0, 2, Method.DRAW_BEND1),
        HarpScaleItem(1, 2, Method.DRAW_BEND2),
        HarpScaleItem(3, 2, Method.DRAW),
        HarpScaleItem(3, 3, Method.BLOW),
        HarpScaleItem(4, 3, Method.DRAW_BEND3),
        HarpScaleItem(5, 3, Method.DRAW_BEND2),
        HarpScaleItem(6, 3, Method.DRAW_BEND1),
        HarpScaleItem(7, 3, Method.DRAW),
        HarpScaleItem(29, 10, Method.DRAW),
        HarpScaleItem(32, 10, Method.BLOW),
    ]

    assert get_harp_scale(harp_scale, blowbend=True) == [
        HarpScaleItem(0, 2, Method.BLOW),
        HarpScaleItem(3, 2, Method.DRAW),
        HarpScaleItem(3, 3, Method.BLOW),
        HarpScaleItem(7, 3, Method.DRAW),
        HarpScaleItem(29, 10, Method.DRAW),
        HarpScaleItem(30, 10, Method.BLOW_BEND2),
        HarpScaleItem(31, 10, Method.BLOW_BEND1),
        HarpScaleItem(32, 10, Method.BLOW),
    ]

    assert get_harp_scale(harp_scale, overblow=True) == [
        HarpScaleItem(0, 2, Method.BLOW),
        HarpScaleItem(3, 2, Method.DRAW),
        HarpScaleItem(3, 3, Method.BLOW),
        HarpScaleItem(7, 3, Method.DRAW),
        HarpScaleItem(18, 6, Method.OVERBLOW),
        HarpScaleItem(29, 10, Method.DRAW),
        HarpScaleItem(32, 10, Method.BLOW),
    ]

    assert get_harp_scale(harp_scale, overdraw=True) == [
        HarpScaleItem(0, 2, Method.BLOW),
        HarpScaleItem(3, 2, Method.DRAW),
        HarpScaleItem(3, 3, Method.BLOW),
        HarpScaleItem(7, 3, Method.DRAW),
        HarpScaleItem(29, 10, Method.DRAW),
        HarpScaleItem(32, 10, Method.BLOW),
        HarpScaleItem(33, 10, Method.OVERDRAW),
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
        [[HarpScaleItem(0, 1, Method.BLOW)], [HarpScaleItem(36, 10, Method.BLOW)]],
    ]

    assert _get_score_layout([0,7,36], richter_diatonic_scale) == [
       [
           [HarpScaleItem(0, 1, Method.BLOW)],
           [HarpScaleItem(7, 3, Method.BLOW), HarpScaleItem(7, 2, Method.DRAW)], # 2 options for the pitch
           [HarpScaleItem(36, 10, Method.BLOW)],
       ],
    ]

    assert _get_score_layout([1,8,37], richter_diatonic_scale) == [
       [
           [HarpScaleItem(0, 1, Method.BLOW)],
           [HarpScaleItem(7, 3, Method.BLOW), HarpScaleItem(7, 2, Method.DRAW)], # 2 options for the pitch
           [HarpScaleItem(36, 10, Method.BLOW)],
       ],
    ]

    assert _get_score_layout([1,3,5], richter_diatonic_scale) == [
       [
           [HarpScaleItem(0, 1, Method.BLOW,),],
           [HarpScaleItem(2, 1, Method.DRAW,),],
           [HarpScaleItem(4, 2, Method.BLOW,),],
       ],
       [
           [HarpScaleItem(12, 4, Method.BLOW,),],
           [HarpScaleItem(14, 4, Method.DRAW,),],
           [HarpScaleItem(16, 5, Method.BLOW,),],
       ],
       [
           [HarpScaleItem(17, 5, Method.DRAW,),],
           [HarpScaleItem(19, 6, Method.BLOW,),],
           [HarpScaleItem(21, 6, Method.DRAW,),],
       ],
       [
           [HarpScaleItem(19, 6, Method.BLOW,),],
           [HarpScaleItem(21, 6, Method.DRAW,),],
           [HarpScaleItem(23, 7, Method.DRAW,),],
       ],
       [
           [HarpScaleItem(24, 7, Method.BLOW,),],
           [HarpScaleItem(26, 8, Method.DRAW,),],
           [HarpScaleItem(28, 8, Method.BLOW,),],
       ],
       [
           [HarpScaleItem(29, 9, Method.DRAW,),],
           [HarpScaleItem(31, 9, Method.BLOW,),],
           [HarpScaleItem(33, 10, Method.DRAW,),],
       ],
   ]

import pytest
from harmonicas import Pitch
from harp_utils import  _match_harp_to_score, _get_score_layout, get_harp_scale
from harmonicas import Method

richter_full_scale = [
    (0, 1, Method.BLOW),
    (1, 1, Method.DRAW_BEND1),
    (2, 1, Method.DRAW),
    (3, 1, Method.OVERBLOW),
    (4, 2, Method.BLOW),
    (5, 2, Method.DRAW_BEND2),
    (7, 2, Method.DRAW),
    (7, 3, Method.BLOW),
    (8, 3, Method.DRAW_BEND3),
    (9, 3, Method.DRAW_BEND2),
    (10, 3, Method.DRAW_BEND1),
    (11, 3, Method.DRAW),
    (12, 4, Method.BLOW),
    (13, 4, Method.DRAW_BEND1),
    (14, 4, Method.DRAW),
    (15, 4, Method.OVERBLOW),
    (16, 5, Method.BLOW),
    (17, 5, Method.DRAW),
    (18, 5, Method.OVERBLOW),
    (19, 6, Method.BLOW),
    (20, 6, Method.DRAW_BEND1),
    (21, 6, Method.DRAW),
    (22, 6, Method.OVERBLOW),
    (23, 7, Method.DRAW),
    (24, 7, Method.BLOW),
    (26, 8, Method.DRAW),
    (27, 8, Method.BLOW_BEND1),
    (28, 8, Method.BLOW),
    (29, 9, Method.DRAW),
    (30, 9, Method.BLOW_BEND1),
    (31, 9, Method.BLOW),
    (32, 9, Method.OVERDRAW),
    (33, 10, Method.DRAW),
    (34, 10, Method.BLOW_BEND2),
    (35, 10, Method.BLOW_BEND1),
    (36, 10, Method.BLOW),
    (37, 10, Method.OVERDRAW)
]


richter_diatonic_scale = [
    (0, 1, Method.BLOW),
    (2, 1, Method.DRAW),
    (4, 2, Method.BLOW),
    (7, 2, Method.DRAW),
    (7, 3, Method.BLOW),
    (11, 3, Method.DRAW),
    (12, 4, Method.BLOW),
    (14, 4, Method.DRAW),
    (16, 5, Method.BLOW),
    (17, 5, Method.DRAW),
    (19, 6, Method.BLOW),
    (21, 6, Method.DRAW),
    (23, 7, Method.DRAW),
    (24, 7, Method.BLOW),
    (26, 8, Method.DRAW),
    (28, 8, Method.BLOW),
    (29, 9, Method.DRAW),
    (31, 9, Method.BLOW),
    (33, 10, Method.DRAW),
    (36, 10, Method.BLOW),
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
        (0, 2, Method.BLOW),
        (3, 2, Method.DRAW),
        (3, 3, Method.BLOW),
        (7, 3, Method.DRAW),
        (29, 10, Method.DRAW),
        (32, 10, Method.BLOW),
    ]

    assert get_harp_scale(harp_scale, drawbend=True) == [
        (0, 2, Method.BLOW),
        (0, 2, Method.DRAW_BEND1),
        (1, 2, Method.DRAW_BEND2),
        (3, 2, Method.DRAW),
        (3, 3, Method.BLOW),
        (4, 3, Method.DRAW_BEND3),
        (5, 3, Method.DRAW_BEND2),
        (6, 3, Method.DRAW_BEND1),
        (7, 3, Method.DRAW),
        (29, 10, Method.DRAW),
        (32, 10, Method.BLOW),
    ]

    assert get_harp_scale(harp_scale, blowbend=True) == [
        (0, 2, Method.BLOW),
        (3, 2, Method.DRAW),
        (3, 3, Method.BLOW),
        (7, 3, Method.DRAW),
        (29, 10, Method.DRAW),
        (30, 10, Method.BLOW_BEND2),
        (31, 10, Method.BLOW_BEND1),
        (32, 10, Method.BLOW),
    ]

    assert get_harp_scale(harp_scale, overblow=True) == [
        (0, 2, Method.BLOW),
        (3, 2, Method.DRAW),
        (3, 3, Method.BLOW),
        (7, 3, Method.DRAW),
        (18, 6, Method.OVERBLOW),
        (29, 10, Method.DRAW),
        (32, 10, Method.BLOW),
    ]

    assert get_harp_scale(harp_scale, overdraw=True) == [
        (0, 2, Method.BLOW),
        (3, 2, Method.DRAW),
        (3, 3, Method.BLOW),
        (7, 3, Method.DRAW),
        (29, 10, Method.DRAW),
        (32, 10, Method.BLOW),
        (33, 10, Method.OVERDRAW),
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
        [[(0, 1, Method.BLOW)], [(36, 10, Method.BLOW)]],
    ]

    assert _get_score_layout([0,7,36], richter_diatonic_scale) == [
       [
           [(0, 1, Method.BLOW)],
           [(7, 3, Method.BLOW), (7, 2, Method.DRAW)], # 2 options for the pitch
           [(36, 10, Method.BLOW)],
       ],
    ]

    assert _get_score_layout([1,8,37], richter_diatonic_scale) == [
       [
           [(0, 1, Method.BLOW)],
           [(7, 3, Method.BLOW), (7, 2, Method.DRAW)], # 2 options for the pitch
           [(36, 10, Method.BLOW)],
       ],
    ]

    assert _get_score_layout([1,3,5], richter_diatonic_scale) == [
       [
           [(0, 1, Method.BLOW,),],
           [(2, 1, Method.DRAW,),],
           [(4, 2, Method.BLOW,),],
       ],
       [
           [(12, 4, Method.BLOW,),],
           [(14, 4, Method.DRAW,),],
           [(16, 5, Method.BLOW,),],
       ],
       [
           [(17, 5, Method.DRAW,),],
           [(19, 6, Method.BLOW,),],
           [(21, 6, Method.DRAW,),],
       ],
       [
           [(19, 6, Method.BLOW,),],
           [(21, 6, Method.DRAW,),],
           [(23, 7, Method.DRAW,),],
       ],
       [
           [(24, 7, Method.BLOW,),],
           [(26, 8, Method.DRAW,),],
           [(28, 8, Method.BLOW,),],
       ],
       [
           [(29, 9, Method.DRAW,),],
           [(31, 9, Method.BLOW,),],
           [(33, 10, Method.DRAW,),],
       ],
   ]

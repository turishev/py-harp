import pytest
from harmonicas import Pitch, Method
from harp_utils import HarpPitch,_match_harp_to_score, get_harp_scale, get_harp_key, get_scale_note, get_harp_scale_degrees, scale_to_layout


richter_full_scale = [
    HarpPitch(0, 1, False, Method.BLOW),
    HarpPitch(1, 1, False, Method.DRAW_BEND1),
    HarpPitch(2, 1, False, Method.DRAW),
    HarpPitch(3, 1, False, Method.OVERBLOW),
    HarpPitch(4, 2, False, Method.BLOW),
    HarpPitch(5, 2, False, Method.DRAW_BEND2),
    HarpPitch(7, 2, False, Method.DRAW),
    HarpPitch(7, 3, False, Method.BLOW),
    HarpPitch(8, 3, False, Method.DRAW_BEND3),
    HarpPitch(9, 3, False, Method.DRAW_BEND2),
    HarpPitch(10, 3, False, Method.DRAW_BEND1),
    HarpPitch(11, 3, False, Method.DRAW),
    HarpPitch(12, 4, False, Method.BLOW),
    HarpPitch(13, 4, False, Method.DRAW_BEND1),
    HarpPitch(14, 4, False, Method.DRAW),
    HarpPitch(15, 4, False, Method.OVERBLOW),
    HarpPitch(16, 5, False, Method.BLOW),
    HarpPitch(17, 5, False, Method.DRAW),
    HarpPitch(18, 5, False, Method.OVERBLOW),
    HarpPitch(19, 6, False, Method.BLOW),
    HarpPitch(20, 6, False, Method.DRAW_BEND1),
    HarpPitch(21, 6, False, Method.DRAW),
    HarpPitch(22, 6, False, Method.OVERBLOW),
    HarpPitch(23, 7, False, Method.DRAW),
    HarpPitch(24, 7, False, Method.BLOW),
    HarpPitch(26, 8, False, Method.DRAW),
    HarpPitch(27, 8, False, Method.BLOW_BEND1),
    HarpPitch(28, 8, False, Method.BLOW),
    HarpPitch(29, 9, False, Method.DRAW),
    HarpPitch(30, 9, False, Method.BLOW_BEND1),
    HarpPitch(31, 9, False, Method.BLOW),
    HarpPitch(32, 9, False, Method.OVERDRAW),
    HarpPitch(33, 10, False, Method.DRAW),
    HarpPitch(34, 10, False, Method.BLOW_BEND2),
    HarpPitch(35, 10, False, Method.BLOW_BEND1),
    HarpPitch(36, 10, False, Method.BLOW),
    HarpPitch(37, 10, False, Method.OVERDRAW)
]


richter_diatonic_scale = [
    HarpPitch(0, 1, False, Method.BLOW),
    HarpPitch(2, 1, False, Method.DRAW),
    HarpPitch(4, 2, False, Method.BLOW),
    HarpPitch(7, 2, False, Method.DRAW),
    HarpPitch(7, 3, False, Method.BLOW),
    HarpPitch(11, 3, False, Method.DRAW),
    HarpPitch(12, 4, False, Method.BLOW),
    HarpPitch(14, 4, False, Method.DRAW),
    HarpPitch(16, 5, False, Method.BLOW),
    HarpPitch(17, 5, False, Method.DRAW),
    HarpPitch(19, 6, False, Method.BLOW),
    HarpPitch(21, 6, False, Method.DRAW),
    HarpPitch(23, 7, False, Method.DRAW),
    HarpPitch(24, 7, False, Method.BLOW),
    HarpPitch(26, 8, False, Method.DRAW),
    HarpPitch(28, 8, False, Method.BLOW),
    HarpPitch(29, 9, False, Method.DRAW),
    HarpPitch(31, 9, False, Method.BLOW),
    HarpPitch(33, 10, False, Method.DRAW),
    HarpPitch(36, 10, False, Method.BLOW),
]



harp_part_scale = [# part of richer scale
        Pitch(10, False,  Method.DRAW,  '6/3'),
        Pitch(10, False,  Method.BLOW_BEND2,  '7b/3'),
        Pitch(10, False,  Method.BLOW_BEND1,  '7/3'),
        Pitch(10, False,  Method.BLOW,  '1/4'),
        Pitch(10, False,  Method.OVERDRAW,  '2b/4'),

        Pitch(2, False,  Method.BLOW,  '3/1'),
        Pitch(2, False,  Method.DRAW_BEND2,  '4/1'),
        Pitch(2, False,  Method.DRAW_BEND1,  '4b/1'),
        Pitch(2, False,  Method.DRAW,  '5/1'),

        Pitch(3, False,  Method.BLOW,  '5/1'),
        Pitch(3, False,  Method.DRAW_BEND3,  '6b/1'),
        Pitch(3, False,  Method.DRAW_BEND2,  '6/1'),
        Pitch(3, False,  Method.DRAW_BEND1,  '7b/1'),
        Pitch(3, False,  Method.DRAW,  '7/1'),

        Pitch(6, False,  Method.OVERBLOW,  '7b/2'),
]



def test_get_harp_key():
    assert get_harp_key(1, "g") == "g"
    assert get_harp_key(2, "g") == "c"
    assert get_harp_key(3, "g") == "f"

def test_get_scale_note():
    assert get_scale_note("c", "1") == "c"
    assert get_scale_note("c", "3b") == "eb"
    assert get_scale_note("c", "3b/4") == "eb"
    assert get_scale_note("c", "7") == "b"
    assert get_scale_note("c", "7#") == "c"
    assert get_scale_note("g", "1") == "g"
    assert get_scale_note("g", "1/2") == "g"


def test_get_harp_scale_degrees():
    assert get_harp_scale_degrees(get_harp_scale(harp_part_scale)) == [4, 7, 11, 33, 36]

    
def test_get_harp_scale():
    assert get_harp_scale(harp_part_scale) == [
        HarpPitch(4, 2, False, Method.BLOW),
        HarpPitch(7, 2, False, Method.DRAW),
        HarpPitch(7, 3, False, Method.BLOW),
        HarpPitch(11, 3, False, Method.DRAW),
        HarpPitch(33, 10, False, Method.DRAW),
        HarpPitch(36, 10, False, Method.BLOW),
    ]

    assert get_harp_scale(harp_part_scale, drawbend=True) == [
        HarpPitch(4, 2, False, Method.BLOW),
        HarpPitch(4, 2, False, Method.DRAW_BEND1),
        HarpPitch(5, 2, False, Method.DRAW_BEND2),
        HarpPitch(7, 2, False, Method.DRAW),
        HarpPitch(7, 3, False, Method.BLOW),
        HarpPitch(8, 3, False, Method.DRAW_BEND3),
        HarpPitch(9, 3, False, Method.DRAW_BEND2),
        HarpPitch(10, 3, False, Method.DRAW_BEND1),
        HarpPitch(11, 3, False, Method.DRAW),
        HarpPitch(33, 10, False, Method.DRAW),
        HarpPitch(36, 10, False, Method.BLOW),
    ]

    assert get_harp_scale(harp_part_scale, blowbend=True) == [
        HarpPitch(4, 2, False, Method.BLOW),
        HarpPitch(7, 2, False, Method.DRAW),
        HarpPitch(7, 3, False, Method.BLOW),
        HarpPitch(11, 3, False, Method.DRAW),
        HarpPitch(33, 10, False, Method.DRAW),
        HarpPitch(34, 10, False, Method.BLOW_BEND2),
        HarpPitch(35, 10, False, Method.BLOW_BEND1),
        HarpPitch(36, 10, False, Method.BLOW),
    ]

    assert get_harp_scale(harp_part_scale, overblow=True) == [
        HarpPitch(4, 2, False, Method.BLOW),
        HarpPitch(7, 2, False, Method.DRAW),
        HarpPitch(7, 3, False, Method.BLOW),
        HarpPitch(11, 3, False, Method.DRAW),
        HarpPitch(22, 6, False, Method.OVERBLOW),
        HarpPitch(33, 10, False, Method.DRAW),
        HarpPitch(36, 10, False, Method.BLOW),
    ]

    assert get_harp_scale(harp_part_scale, overdraw=True) == [
        HarpPitch(4, 2, False, Method.BLOW),
        HarpPitch(7, 2, False, Method.DRAW),
        HarpPitch(7, 3, False, Method.BLOW),
        HarpPitch(11, 3, False, Method.DRAW),
        HarpPitch(33, 10, False, Method.DRAW),
        HarpPitch(36, 10, False, Method.BLOW),
        HarpPitch(37, 10, False, Method.OVERDRAW),
    ]



def test_match_harp_to_score():
    # richer diatonic scale
    richter_diatonic = [0,2,4,7,11,12,14,16,17,19,21,23,24,26,28,29,31,33,36]
    # major chord
    assert _match_harp_to_score([0,4,7], richter_diatonic) == [
        (0, [0, 4, 7, 12, 16, 19, 24, 28, 31, 36]), # 1st position - root = 0,12,24,36
        (7, [2, 7, 11, 14, 19, 23, 26, 31]) # 2st position - root = 7,19,31
    ]

    # octaves test
    assert _match_harp_to_score([0,36], richter_diatonic) == [
        (0, [0, 12, 24, 36]),
    ]

    assert _match_harp_to_score(richter_diatonic, richter_diatonic) == [(0, richter_diatonic)]
        
    # simple_match test
    assert _match_harp_to_score([0,4,7], richter_diatonic, simple_match=True) == [
        (0, [0, 4, 7]), # 1st position - root = 0,12,24,36
        (7, [7, 11, 14]) # 2st position - root = 7,19,31
    ]

    orchestra_s_diatonic = [
        7, 9, 11, 12, 14, 16, 17, 19, 21, 23, 24, 26, 28, 29, 31, 33, 35, 36]

    assert _match_harp_to_score([0,4,7], orchestra_s_diatonic, simple_match=True) == [
        (7, [7, 11, 14]),
        (12, [12, 16, 19]), 
        (17, [17, 21, 24]), 
        (24, [24, 28, 31]), 
        (29, [29, 33, 36])
    ] 

    assert _match_harp_to_score([0,4,7], orchestra_s_diatonic) == [
        (7, [7, 11, 14, 19, 23, 26, 31, 35]),
        (12, [7, 12, 16, 19, 24, 28, 31, 36]), 
        (17, [9, 12, 17, 21, 24, 29, 33, 36]), 
        (24, [12, 16, 19, 24, 28, 31, 36]), 
        (29, [17, 21, 24, 29, 33, 36])
    ] 

    # 7-chord - 3,5,7b
    assert _match_harp_to_score([4,7,10], orchestra_s_diatonic) == [
        (7, [11, 14, 17, 23, 26, 29, 35])
    ]

    assert _match_harp_to_score([4,7,10], orchestra_s_diatonic, True) == [
        (7, [11, 14, 17])
    ]

def test_scale_to_layout():
    # major chord
    assert scale_to_layout('richter', [0,4,7]) == [
        (1, [
            (0, [HarpPitch(0, 1, False, Method.BLOW)]),
            (4, [HarpPitch(4, 2, False, Method.BLOW)]),
            (7, [HarpPitch(7, 2, False, Method.DRAW),
                 HarpPitch(7, 3, False, Method.BLOW)]),
            (12, [HarpPitch(12, 4, False, Method.BLOW)]),
            (16, [HarpPitch(16, 5, False, Method.BLOW)]),
            (19, [HarpPitch(19, 6, False, Method.BLOW)]),
            (24, [HarpPitch(24, 7, False, Method.BLOW)]),
            (28, [HarpPitch(28, 8, False, Method.BLOW)]),
            (31, [HarpPitch(31, 9, False, Method.BLOW)]),
            (36, [HarpPitch(36, 10, False, Method.BLOW)]),
        ]),
        (2, [
            (-5, [HarpPitch(2, 1, False, Method.DRAW)]),
            (0, [HarpPitch(7, 2, False, Method.DRAW),
                 HarpPitch(7, 3, False, Method.BLOW)]),
            (4, [HarpPitch(11, 3, False, Method.DRAW)]),
            (7, [HarpPitch(14, 4, False, Method.DRAW)]),
            (12, [HarpPitch(19, 6, False, Method.BLOW)]),
            (16, [HarpPitch(23, 7, False, Method.DRAW)]),
            (19, [HarpPitch(26, 8, False, Method.DRAW)]),
            (24, [HarpPitch(31, 9, False, Method.BLOW)]),
        ])
    ]

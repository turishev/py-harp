import pytest
from harmonicas import Pitch, Method
from harp_utils import HarpPitch,_match_harp_to_score, _get_score_layout, get_harp_scale, get_harp_key
from score import split_note, parse_step, parse_note, parse_score

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

def test_split_note():
    assert split_note("1") == ("1",0,1) 
    assert split_note("1#") == ("1",1,1) 
    assert split_note("1b") == ("1",-1,1) 
    assert split_note("1/1") == ("1",0,1) 
    assert split_note("1#/1") == ("1",1,1) 
    assert split_note("1b/1") == ("1",-1,1) 
    assert split_note("1/2") == ("1",0,2) 
    assert split_note("1#/2") == ("1",1,2) 
    assert split_note("1b/2") == ("1",-1,2)  
    assert split_note("3/2") == ("3",0,2) 
    assert split_note("3#/2") == ("3",1,2) 
    assert split_note("3b/2") == ("3",-1,2) 
    assert split_note("b/2") == ("b",0,2) 
    assert split_note("b#/2") == ("b",1,2) 
    assert split_note("bb/2") == ("b",-1,2) 


def test_parse_step():
    assert parse_step("1") == 0
    assert parse_step("1b") == -1
    assert parse_step("1#") == 1
    assert parse_step("1/1") == 0
    assert parse_step("1b/1") == -1
    assert parse_step("1#/1") == 1
    assert parse_step("7") == 11
    assert parse_step("7b") == 10
    assert parse_step("7#") == 12
    assert parse_step("1/2") == 12
    assert parse_step("1b/2") == 11
    assert parse_step("1#/2") == 13
    # assert parse_step("8") == 12 not allowed at now
    assert parse_step("7#/2") == 24

def test_parse_note():
    assert parse_note("c") == 0
    assert parse_note("cb") == -1
    assert parse_note("c#") == 1
    assert parse_note("c/1") == 0
    assert parse_note("cb/1") == -1
    assert parse_note("c#/1") == 1
    assert parse_note("d") == 2
    assert parse_note("b") == 11
    assert parse_note("bb") == 10
    assert parse_note("b#") == 12
    assert parse_note("c/2") == 12
    assert parse_note("cb/2") == 11
    assert parse_note("c#/2") == 13
    assert parse_note("b#/2") == 24
    assert parse_note("B#/2") == 24


def test_parse_score():
    assert parse_score("c,d,e,f,g,a,b", "c") == [0, 2, 4, 5, 7, 9, 11]
    assert parse_score("c,d,e,f,g,a,b", "a") == [3, 5, 7, 8, 10, 12, 14]
    assert parse_score("c,a,a/2", "a/2") == [3, 12, 24]


def test_get_harp_scale():
    harp_scale = [# part of richer scale
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

    assert get_harp_scale(harp_scale) == [
        HarpPitch(0, 2, False, Method.BLOW),
        HarpPitch(3, 2, False, Method.DRAW),
        HarpPitch(3, 3, False, Method.BLOW),
        HarpPitch(7, 3, False, Method.DRAW),
        HarpPitch(29, 10, False, Method.DRAW),
        HarpPitch(32, 10, False, Method.BLOW),
    ]

    assert get_harp_scale(harp_scale, drawbend=True) == [
        HarpPitch(0, 2, False, Method.BLOW),
        HarpPitch(0, 2, False, Method.DRAW_BEND1),
        HarpPitch(1, 2, False, Method.DRAW_BEND2),
        HarpPitch(3, 2, False, Method.DRAW),
        HarpPitch(3, 3, False, Method.BLOW),
        HarpPitch(4, 3, False, Method.DRAW_BEND3),
        HarpPitch(5, 3, False, Method.DRAW_BEND2),
        HarpPitch(6, 3, False, Method.DRAW_BEND1),
        HarpPitch(7, 3, False, Method.DRAW),
        HarpPitch(29, 10, False, Method.DRAW),
        HarpPitch(32, 10, False, Method.BLOW),
    ]

    assert get_harp_scale(harp_scale, blowbend=True) == [
        HarpPitch(0, 2, False, Method.BLOW),
        HarpPitch(3, 2, False, Method.DRAW),
        HarpPitch(3, 3, False, Method.BLOW),
        HarpPitch(7, 3, False, Method.DRAW),
        HarpPitch(29, 10, False, Method.DRAW),
        HarpPitch(30, 10, False, Method.BLOW_BEND2),
        HarpPitch(31, 10, False, Method.BLOW_BEND1),
        HarpPitch(32, 10, False, Method.BLOW),
    ]

    assert get_harp_scale(harp_scale, overblow=True) == [
        HarpPitch(0, 2, False, Method.BLOW),
        HarpPitch(3, 2, False, Method.DRAW),
        HarpPitch(3, 3, False, Method.BLOW),
        HarpPitch(7, 3, False, Method.DRAW),
        HarpPitch(18, 6, False, Method.OVERBLOW),
        HarpPitch(29, 10, False, Method.DRAW),
        HarpPitch(32, 10, False, Method.BLOW),
    ]

    assert get_harp_scale(harp_scale, overdraw=True) == [
        HarpPitch(0, 2, False, Method.BLOW),
        HarpPitch(3, 2, False, Method.DRAW),
        HarpPitch(3, 3, False, Method.BLOW),
        HarpPitch(7, 3, False, Method.DRAW),
        HarpPitch(29, 10, False, Method.DRAW),
        HarpPitch(32, 10, False, Method.BLOW),
        HarpPitch(33, 10, False, Method.OVERDRAW),
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
        [[HarpPitch(0, 1, False, Method.BLOW)], [HarpPitch(36, 10, False, Method.BLOW)]],
    ]

    assert _get_score_layout([0,7,36], richter_diatonic_scale) == [
       [
           [HarpPitch(0, 1, False, Method.BLOW)],
           [HarpPitch(7, 3, False, Method.BLOW), HarpPitch(7, 2, False, Method.DRAW)], # 2 options for the pitch
           [HarpPitch(36, 10, False, Method.BLOW)],
       ],
    ]

    assert _get_score_layout([1,8,37], richter_diatonic_scale) == [
       [
           [HarpPitch(0, 1, False, Method.BLOW)],
           [HarpPitch(7, 3, False, Method.BLOW), HarpPitch(7, 2, False, Method.DRAW)], # 2 options for the pitch
           [HarpPitch(36, 10, False, Method.BLOW)],
       ],
    ]

    assert _get_score_layout([1,3,5], richter_diatonic_scale) == [
       [
           [HarpPitch(0, 1, False, Method.BLOW,),],
           [HarpPitch(2, 1, False, Method.DRAW,),],
           [HarpPitch(4, 2, False, Method.BLOW,),],
       ],
       [
           [HarpPitch(12, 4, False, Method.BLOW,),],
           [HarpPitch(14, 4, False, Method.DRAW,),],
           [HarpPitch(16, 5, False, Method.BLOW,),],
       ],
       [
           [HarpPitch(17, 5, False, Method.DRAW,),],
           [HarpPitch(19, 6, False, Method.BLOW,),],
           [HarpPitch(21, 6, False, Method.DRAW,),],
       ],
       [
           [HarpPitch(19, 6, False, Method.BLOW,),],
           [HarpPitch(21, 6, False, Method.DRAW,),],
           [HarpPitch(23, 7, False, Method.DRAW,),],
       ],
       [
           [HarpPitch(24, 7, False, Method.BLOW,),],
           [HarpPitch(26, 8, False, Method.DRAW,),],
           [HarpPitch(28, 8, False, Method.BLOW,),],
       ],
       [
           [HarpPitch(29, 9, False, Method.DRAW,),],
           [HarpPitch(31, 9, False, Method.BLOW,),],
           [HarpPitch(33, 10, False, Method.DRAW,),],
       ],
   ]

def test_get_harp_key():
    assert get_harp_key(1, "g") == "g"
    assert get_harp_key(2, "g") == "c"
    assert get_harp_key(3, "g") == "f"
    

import enum
from dataclasses import dataclass

@enum.unique
class Method(enum.Enum):
    BLOW = 0
    DRAW = 1
    DRAW_BEND1 = 2
    DRAW_BEND2 = 3
    DRAW_BEND3 = 4
    BLOW_BEND1 = 5
    BLOW_BEND2 = 6
    BLOW_BEND3 = 7
    OVERBLOW = 8
    OVERDRAW = 9
    

@dataclass(frozen=True, slots=True)
class Pitch:
    hole : int
    slide : bool
    method : Method
    pitch : str

known_harmonicas_list = {
    'richter' : {
        'description':'the diatonic standard richter tuning',
        'scale' : [
            Pitch(1, False,  Method.BLOW,  '1/1'),
            Pitch(1, False,  Method.DRAW_BEND1,  '2b/1'),
            Pitch(1, False,  Method.DRAW,  '2/1'),
            Pitch(1, False,  Method.OVERBLOW,  '3b/1'),

            Pitch(2, False,  Method.BLOW,  '3/1'),
            Pitch(2, False,  Method.DRAW_BEND2,  '4/1'),
            Pitch(2, False,  Method.DRAW_BEND1,  '4b/1'),
            Pitch(2, False,  Method.DRAW,  '5/1'),

            Pitch(3, False,  Method.BLOW,  '5/1'),
            Pitch(3, False,  Method.DRAW_BEND3,  '6b/1'),
            Pitch(3, False,  Method.DRAW_BEND2,  '6/1'),
            Pitch(3, False,  Method.DRAW_BEND1,  '7b/1'),
            Pitch(3, False,  Method.DRAW,  '7/1'),

            Pitch(4, False,  Method.BLOW,  '1/2'),
            Pitch(4, False,  Method.DRAW_BEND1,  '2b/2'),
            Pitch(4, False,  Method.DRAW,  '2/2'),
            Pitch(4, False,  Method.OVERBLOW,  '3b/2'),

            Pitch(5, False,  Method.BLOW,  '3/2'),
            Pitch(5, False,  Method.DRAW,  '4/2'),
            Pitch(5, False,  Method.OVERBLOW,  '5b/2'),

            Pitch(6, False,  Method.BLOW,  '5/2'),
            Pitch(6, False,  Method.DRAW_BEND1,  '6b/2'),
            Pitch(6, False,  Method.DRAW,  '6/2'),
            Pitch(6, False,  Method.OVERBLOW,  '7b/2'),

            Pitch(7, False,  Method.DRAW,  '7/2'),
            Pitch(7, False,  Method.BLOW,  '1/3'),

            Pitch(8, False,  Method.DRAW,  '2/3'),
            Pitch(8, False,  Method.BLOW_BEND1,  '3b/3'),
            Pitch(8, False,  Method.BLOW,  '3/3'),

            Pitch(9, False,  Method.DRAW,  '4/3'),
            Pitch(9, False,  Method.BLOW_BEND1,  '5b/3'),
            Pitch(9, False,  Method.BLOW,  '5/3'),
            Pitch(9, False,  Method.OVERDRAW,  '6b/3'),

            Pitch(10, False,  Method.DRAW,  '6/3'),
            Pitch(10, False,  Method.BLOW_BEND2,  '7b/3'),
            Pitch(10, False,  Method.BLOW_BEND1,  '7/3'),
            Pitch(10, False,  Method.BLOW,  '1/4'),
            Pitch(10, False,  Method.OVERDRAW,  '2b/4'),
        ],
    },
    'paddy-richter' : {
        'description':'a Brendan Power tuning, changed 3 blow',
        'scale' : [
            Pitch(1, False,  Method.BLOW,  '1/1'),
            Pitch(1, False,  Method.DRAW_BEND1,  '2b/1'),
            Pitch(1, False,  Method.DRAW,  '2/1'),
            Pitch(1, False,  Method.OVERBLOW,  '3b/1'),

            Pitch(2, False,  Method.BLOW,  '3/1'),
            Pitch(2, False,  Method.DRAW_BEND2,  '4/1'),
            Pitch(2, False,  Method.DRAW_BEND1,  '4b/1'),
            Pitch(2, False,  Method.DRAW,  '5/1'),

            Pitch(3, False,  Method.BLOW,  '6/1'),
            Pitch(3, False,  Method.DRAW_BEND1,  '7b/1'),
            Pitch(3, False,  Method.DRAW,  '7/1'),

            Pitch(4, False,  Method.BLOW,  '1/2'),
            Pitch(4, False,  Method.DRAW_BEND1,  '2b/2'),
            Pitch(4, False,  Method.DRAW,  '2/2'),
            Pitch(4, False,  Method.OVERBLOW,  '3b/2'),

            Pitch(5, False,  Method.BLOW,  '3/2'),
            Pitch(5, False,  Method.DRAW,  '4/2'),
            Pitch(5, False,  Method.OVERBLOW,  '5b/2'),

            Pitch(6, False,  Method.BLOW,  '5/2'),
            Pitch(6, False,  Method.DRAW_BEND1,  '6b/2'),
            Pitch(6, False,  Method.DRAW,  '6/2'),
            Pitch(6, False,  Method.OVERBLOW,  '7b/2'),

            Pitch(7, False,  Method.DRAW,  '7/2'),
            Pitch(7, False,  Method.BLOW,  '1/3'),

            Pitch(8, False,  Method.DRAW,  '2/3'),
            Pitch(8, False,  Method.BLOW_BEND1,  '3b/3'),
            Pitch(8, False,  Method.BLOW,  '3/3'),

            Pitch(9, False,  Method.DRAW,  '4/3'),
            Pitch(9, False,  Method.BLOW_BEND1,  '5b/3'),
            Pitch(9, False,  Method.BLOW,  '5/3'),
            Pitch(9, False,  Method.OVERDRAW,  '6b/3'),

            Pitch(10, False,  Method.DRAW,  '6/3'),
            Pitch(10, False,  Method.BLOW_BEND2,  '7b/3'),
            Pitch(10, False,  Method.BLOW_BEND1,  '7/3'),
            Pitch(10, False,  Method.BLOW,  '1/4'),
            Pitch(10, False,  Method.OVERDRAW,  '2b/4'),
        ],
    },
    'power-bender' : {
        'description':'a Brendan Power tuning',
        'scale': [
            # as in Richer
            Pitch(1, False,  Method.BLOW,  '1/1'),
            Pitch(1, False,  Method.DRAW_BEND1,  '2b/1'),
            Pitch(1, False,  Method.DRAW,  '2/1'),
            Pitch(1, False,  Method.OVERBLOW,  '3b/1'),

            Pitch(2, False,  Method.BLOW,  '3/1'),
            Pitch(2, False,  Method.DRAW_BEND2,  '4/1'),
            Pitch(2, False,  Method.DRAW_BEND1,  '4b/1'),
            Pitch(2, False,  Method.DRAW,  '5/1'),

            Pitch(3, False,  Method.BLOW,  '5/1'),
            Pitch(3, False,  Method.DRAW_BEND3,  '6b/1'),
            Pitch(3, False,  Method.DRAW_BEND2,  '6/1'),
            Pitch(3, False,  Method.DRAW_BEND1,  '7b/1'),
            Pitch(3, False,  Method.DRAW,  '7/1'),

            Pitch(4, False,  Method.BLOW,  '1/2'),
            Pitch(4, False,  Method.DRAW_BEND1,  '2b/2'),
            Pitch(4, False,  Method.DRAW,  '2/2'),
            Pitch(4, False,  Method.OVERBLOW,  '3b/2'),
            # changed pitches
            Pitch(5, False,  Method.BLOW,  '2/2'),
            Pitch(4, False,  Method.DRAW_BEND1,  '3b/2'),
            Pitch(5, False,  Method.DRAW,  '3/2'),

            Pitch(6, False,  Method.BLOW,  '4/2'),
            Pitch(6, False,  Method.DRAW_BEND1,  '5b/2'),
            Pitch(6, False,  Method.DRAW,  '5/2'),
            Pitch(6, False,  Method.OVERBLOW,  '6b/2'),

            Pitch(7, False,  Method.BLOW,  '6/2'),
            Pitch(6, False,  Method.DRAW_BEND1,  '7b/2'),
            Pitch(7, False,  Method.DRAW,  '7/2'),

            Pitch(8, False,  Method.BLOW,  '1/3'),
            Pitch(8, False,  Method.DRAW_BEND1,  '2b/3'),
            Pitch(8, False,  Method.DRAW,  '2/3'),

            Pitch(9, False,  Method.BLOW,  '3/3'),
            Pitch(9, False,  Method.BLOW_BEND1,  '5b/3'),
            Pitch(9, False,  Method.DRAW,  '5/3'),
            Pitch(9, False,  Method.OVERDRAW,  '6b/3'),

            Pitch(10, False,  Method.BLOW,  '6/3'),
            Pitch(10, False,  Method.DRAW_BEND2,  '7b/3'),
            Pitch(10, False,  Method.DRAW_BEND1,  '7/3'),
            Pitch(10, False,  Method.DRAW,  '1/4'),
            Pitch(10, False,  Method.OVERBLOW,  '2b/4'),
        ]
    },
    'melody-maker' : {
        'description':'Lee Oskar (Tombo) harmonicas',
        'scale': [
            Pitch(1, False,  Method.BLOW,  '4/1'),
            Pitch(1, False,  Method.DRAW_BEND1,  '5b/1'),
            Pitch(1, False,  Method.DRAW,  '5/1'),

            Pitch(2, False,  Method.BLOW,  '6/1'),
            Pitch(2, False,  Method.DRAW_BEND2,  '7b/1'),
            Pitch(2, False,  Method.DRAW_BEND1,  '7/1'),
            Pitch(2, False,  Method.DRAW,  '1/2'),

            Pitch(3, False,  Method.BLOW,  '2/2'),
            Pitch(3, False,  Method.DRAW_BEND1,  '3b/2'),
            Pitch(3, False,  Method.DRAW,  '3/2'),

            Pitch(4, False,  Method.BLOW,  '4/3'),
            Pitch(4, False,  Method.DRAW_BEND1,  '5b/3'),
            Pitch(4, False,  Method.DRAW,  '5/3'),

            Pitch(5, False,  Method.BLOW,  '6/3'),
            Pitch(4, False,  Method.DRAW_BEND1,  '7b/3'),
            Pitch(5, False,  Method.DRAW,  '7/3'),

            Pitch(6, False,  Method.BLOW,  '1/3'),
            Pitch(6, False,  Method.DRAW_BEND1,  '2b/3'),
            Pitch(6, False,  Method.DRAW,  '2/3'),

            Pitch(7, False,  Method.DRAW,  '3/3'),
            Pitch(7, False,  Method.BLOW,  '4/3'),

            Pitch(8, False,  Method.DRAW,  '5/3'),
            Pitch(8, False,  Method.BLOW_BEND1,  '6b/3'),
            Pitch(8, False,  Method.BLOW,  '6/3'),

            Pitch(9, False,  Method.DRAW,  '7/3'),
            Pitch(9, False,  Method.BLOW,  '1/4'),

            Pitch(10, False,  Method.DRAW,  '2/4'),
            Pitch(10, False,  Method.BLOW_BEND2,  '3b/4'),
            Pitch(10, False,  Method.BLOW_BEND1,  '3/4'),
            Pitch(10, False,  Method.BLOW,  '4/4'),
        ]
    },
    'penta-harp' : {
        'description':'Hohner Penta Harp - minor pentatonic tuning',
        'scale': [
            Pitch(1, False,  Method.BLOW,  '1/1'),
            Pitch(1, False,  Method.DRAW_BEND2,  '2b/1'),
            Pitch(1, False,  Method.DRAW_BEND1,  '2/1'),
            Pitch(1, False,  Method.DRAW,  '3b/1'),
            Pitch(1, False,  Method.OVERBLOW,  '3/1'),
    
            Pitch(2, False,  Method.BLOW,  '4/1'),
            Pitch(2, False,  Method.DRAW,  '5b/1'),
            
            Pitch(3, False,  Method.BLOW,  '5/1'),
            Pitch(3, False,  Method.DRAW_BEND2,  '6b/1'),
            Pitch(3, False,  Method.DRAW_BEND1,  '6/1'),
            Pitch(3, False,  Method.DRAW,  '7b/1'),
            Pitch(3, False,  Method.OVERBLOW,  '7/1'),
            
            Pitch(4, False,  Method.BLOW,  '1/2'),
            Pitch(4, False,  Method.DRAW_BEND2,  '2b/2'),
            Pitch(4, False,  Method.DRAW_BEND1,  '2/2'),
            Pitch(4, False,  Method.DRAW,  '3b/2'),
            Pitch(4, False,  Method.OVERBLOW,  '3/2'),

            Pitch(5, False,  Method.BLOW,  '4/2'),
            Pitch(5, False,  Method.DRAW,  '5b/2'),
            
            Pitch(6, False,  Method.BLOW,  '5/2'),
            Pitch(6, False,  Method.DRAW_BEND2,  '6b/2'),
            Pitch(6, False,  Method.DRAW_BEND1,  '6/2'),
            Pitch(6, False,  Method.DRAW,  '7b/2'),
            Pitch(6, False,  Method.OVERBLOW,  '7/2'),
            
            Pitch(7, False,  Method.BLOW,  '1/3'),
            Pitch(7, False,  Method.DRAW_BEND2,  '2b/3'),
            Pitch(7, False,  Method.DRAW_BEND1,  '2/3'),
            Pitch(7, False,  Method.DRAW,  '3b/3'),
            Pitch(7, False,  Method.OVERBLOW,  '3/3'),

            Pitch(8, False,  Method.BLOW,  '4/3'),
            Pitch(8, False,  Method.DRAW,  '5b/3'),
            
            Pitch(9, False,  Method.BLOW,  '5/3'),
            Pitch(9, False,  Method.DRAW_BEND2,  '6b/3'),
            Pitch(9, False,  Method.DRAW_BEND1,  '6/3'),
            Pitch(9, False,  Method.DRAW,  '7b/3'),
            Pitch(9, False,  Method.OVERBLOW,  '7/3'),
            
            Pitch(10, False,  Method.BLOW,  '1/4'),
            Pitch(10, False,  Method.DRAW_BEND2,  '2b/4'),
            Pitch(10, False,  Method.DRAW_BEND1,  '2/4'),
            Pitch(10, False,  Method.DRAW,  '3b/4'),
            Pitch(10, False,  Method.OVERBLOW,  '3/4'),
        ],
    },
    'major-cross' : {
        'description': 'Seydel Major Cross Tuning, root is 2 draw (second position)',
        'scale': [
            Pitch(1, False,  Method.BLOW,  '5/1'),
            Pitch(1, False,  Method.DRAW_BEND1,  '6b/1'),
            Pitch(1, False,  Method.DRAW,  '6/1'),
            Pitch(1, False,  Method.OVERBLOW,  '7b/1'),

            Pitch(2, False,  Method.BLOW,  '7/1'),
            Pitch(2, False,  Method.DRAW,  '1/2'),
            Pitch(1, False,  Method.OVERBLOW,  '2b/2'),

            Pitch(3, False,  Method.BLOW,  '2/2'),
            Pitch(3, False,  Method.DRAW_BEND1,  '3b/2'),
            Pitch(3, False,  Method.DRAW,  '3/2'),

            Pitch(4, False,  Method.BLOW,  '4/2'),
            Pitch(4, False,  Method.DRAW_BEND1,  '5b/2'),
            Pitch(4, False,  Method.DRAW,  '5/2'),
            Pitch(4, False,  Method.OVERBLOW,  '6b/2'),

            Pitch(5, False,  Method.BLOW,  '6/2'),
            Pitch(4, False,  Method.DRAW_BEND1,  '7b/2'),
            Pitch(5, False,  Method.DRAW,  '7/2'),

            Pitch(6, False,  Method.BLOW,  '1/3'),
            Pitch(6, False,  Method.DRAW_BEND1,  '2b/3'),
            Pitch(6, False,  Method.DRAW,  '2/3'),
            Pitch(6, False,  Method.OVERBLOW,  '3b/3'),

            Pitch(7, False,  Method.DRAW,  '3/3'),
            Pitch(7, False,  Method.BLOW,  '4/3'),
            Pitch(7, False,  Method.OVERDRAW,  '5b/3'),

            Pitch(8, False,  Method.DRAW,  '5/3'),
            Pitch(8, False,  Method.BLOW_BEND1,  '6b/3'),
            Pitch(8, False,  Method.BLOW,  '6/3'),
            Pitch(8, False,  Method.OVERDRAW,  '7b/3'),

            Pitch(9, False,  Method.DRAW,  '7/3'),
            Pitch(9, False,  Method.BLOW,  '1/4'),
            Pitch(9, False,  Method.OVERDRAW,  '2b/4'),

            Pitch(10, False,  Method.DRAW,  '2/4'),
            Pitch(10, False,  Method.BLOW_BEND1,  '3b/4'),
            Pitch(10, False,  Method.BLOW,  '3/4'),
            Pitch(10, False,  Method.OVERDRAW,  '4/4'),
        ],
    },
    'orchestra-s': {
        'description': 'Saydel Orchestra-S, like a chromatic',
        'scale': [
            Pitch(1, False,  Method.BLOW,  '5/1'),
            Pitch(1, False,  Method.DRAW_BEND1,  '6b/1'),
            Pitch(1, False,  Method.DRAW,  '6/1'),
            Pitch(1, False,  Method.OVERBLOW,  '7b/1'),

            Pitch(2, False,  Method.DRAW,  '7/1'),
            Pitch(2, False,  Method.BLOW,  '1/2'),

            Pitch(3, False,  Method.BLOW,  '1/2'),
            Pitch(3, False,  Method.DRAW_BEND1,  '2b/2'),
            Pitch(3, False,  Method.DRAW,  '2/2'),
            Pitch(3, False,  Method.OVERBLOW,  '3b/2'),

            Pitch(4, False,  Method.BLOW,  '3/2'),
            Pitch(4, False,  Method.DRAW,  '4/2'),
            Pitch(4, False,  Method.OVERBLOW,  '5b/2'),

            Pitch(5, False,  Method.BLOW,  '5/2'),
            Pitch(5, False,  Method.DRAW_BEND1,  '6b/2'),
            Pitch(5, False,  Method.DRAW,  '6/2'),
            Pitch(5, False,  Method.OVERBLOW,  '7b/2'),

            Pitch(6, False,  Method.DRAW,  '7/2'),
            Pitch(6, False,  Method.BLOW,  '1/3'),

            Pitch(7, False,  Method.BLOW,  '1/3'),
            Pitch(7, False,  Method.DRAW_BEND1,  '2b/3'),
            Pitch(7, False,  Method.DRAW,  '2/3'),
            Pitch(7, False,  Method.OVERBLOW,  '3b/3'),

            Pitch(8, False,  Method.BLOW,  '3/3'),
            Pitch(8, False,  Method.DRAW,  '4/3'),
            Pitch(8, False,  Method.OVERBLOW,  '5b/3'),

            Pitch(9, False,  Method.BLOW,  '5/3'),
            Pitch(9, False,  Method.DRAW_BEND1,  '6b/3'),
            Pitch(9, False,  Method.DRAW,  '6/3'),
            Pitch(9, False,  Method.OVERBLOW,  '7b/3'),

            Pitch(10, False,  Method.DRAW,  '7/3'),
            Pitch(10, False,  Method.BLOW,  '1/4'),

        ]
    },
    'solist-pro': {
        'description': 'Saydel Solist Pro (12 hole), like a chromatic',
        'scale': [
            Pitch(1, False,  Method.BLOW,  '1/1'),
            Pitch(1, False,  Method.DRAW_BEND1,  '2b/1'),
            Pitch(1, False,  Method.DRAW,  '2/1'),
            Pitch(1, False,  Method.OVERBLOW,  '3b/1'),

            Pitch(2, False,  Method.BLOW,  '3/1'),
            Pitch(2, False,  Method.DRAW,  '4/1'),
            Pitch(2, False,  Method.OVERBLOW,  '5b/1'),

            Pitch(3, False,  Method.BLOW,  '5/1'),
            Pitch(3, False,  Method.DRAW_BEND1,  '6b/1'),
            Pitch(3, False,  Method.DRAW,  '6/1'),
            Pitch(3, False,  Method.OVERBLOW,  '7b/1'),

            Pitch(4, False,  Method.DRAW,  '7/1'),
            Pitch(4, False,  Method.BLOW,  '1/2'),

            Pitch(5, False,  Method.BLOW,  '1/2'),
            Pitch(5, False,  Method.DRAW_BEND1,  '2b/2'),
            Pitch(5, False,  Method.DRAW,  '2/2'),
            Pitch(5, False,  Method.OVERBLOW,  '3b/2'),

            Pitch(6, False,  Method.BLOW,  '3/2'),
            Pitch(6, False,  Method.DRAW,  '4/2'),
            Pitch(6, False,  Method.OVERBLOW,  '5b/2'),

            Pitch(7, False,  Method.BLOW,  '5/2'),
            Pitch(7, False,  Method.DRAW_BEND1,  '6b/2'),
            Pitch(7, False,  Method.DRAW,  '6/2'),
            Pitch(7, False,  Method.OVERBLOW,  '7b/2'),

            Pitch(8, False,  Method.DRAW,  '7/2'),
            Pitch(8, False,  Method.BLOW,  '1/3'),

            Pitch(9, False,  Method.BLOW,  '1/3'),
            Pitch(9, False,  Method.DRAW_BEND1,  '2b/3'),
            Pitch(9, False,  Method.DRAW,  '2/3'),
            Pitch(9, False,  Method.OVERBLOW,  '3b/3'),

            Pitch(10, False,  Method.BLOW,  '3/3'),
            Pitch(10, False,  Method.DRAW,  '4/3'),
            Pitch(10, False,  Method.OVERBLOW,  '5b/3'),

            Pitch(11, False,  Method.BLOW,  '5/3'),
            Pitch(11, False,  Method.DRAW_BEND1,  '6b/3'),
            Pitch(11, False,  Method.DRAW,  '6/3'),
            Pitch(11, False,  Method.OVERBLOW,  '7b/3'),

            Pitch(12, False,  Method.DRAW,  '7/3'),
            Pitch(12, False,  Method.BLOW,  '1/4'),
        ]
    },
    'natural-minor' : {
        'description' : 'Lee Oskar Natural Minor, root is 2 draw (second position)',
        'scale' : [
            Pitch(1, False,  Method.BLOW,  '4/1'),
            Pitch(1, False,  Method.DRAW_BEND1,  '5b/1'),
            Pitch(1, False,  Method.DRAW,  '5/1'),

            Pitch(2, False,  Method.BLOW,  '6b/1'),
            Pitch(2, False,  Method.DRAW_BEND3,  '6/1'),
            Pitch(2, False,  Method.DRAW_BEND2,  '7b/1'),
            Pitch(2, False,  Method.DRAW_BEND1,  '7/1'),
            Pitch(2, False,  Method.DRAW,  '1/2'),

            Pitch(3, False,  Method.BLOW,  '1/2'),
            Pitch(3, False,  Method.DRAW_BEND2,  '2b/2'),
            Pitch(3, False,  Method.DRAW_BEND1,  '2/2'),
            Pitch(3, False,  Method.DRAW,  '3b/2'),
            Pitch(3, False,  Method.OVERBLOW,  '3/2'),

            Pitch(4, False,  Method.BLOW,  '4/2'),
            Pitch(4, False,  Method.DRAW_BEND1,  '5b/2'),
            Pitch(4, False,  Method.DRAW,  '5/2'),
            Pitch(4, False,  Method.OVERBLOW,  '6b/2'),

            Pitch(5, False,  Method.BLOW,  '6b/2'),
            Pitch(5, False,  Method.DRAW_BEND1,  '6/2'),
            Pitch(5, False,  Method.DRAW,  '7b/2'),
            Pitch(5, False,  Method.OVERBLOW,  '7/2'),

            Pitch(6, False,  Method.BLOW,  '1/3'),
            Pitch(6, False,  Method.DRAW_BEND1,  '2b/3'),
            Pitch(6, False,  Method.DRAW,  '2/3'),

            Pitch(7, False,  Method.DRAW,  '3b/3'),
            Pitch(7, False,  Method.BLOW,  '4/3'),
            Pitch(7, False,  Method.OVERDRAW,  '5b/3'),

            Pitch(8, False,  Method.DRAW,  '5/3'),
            Pitch(8, False,  Method.BLOW,  '6b/3'),

            Pitch(9, False,  Method.DRAW,  '7b/3'),
            Pitch(9, False,  Method.BLOW_BEND1,  '7/3'),
            Pitch(9, False,  Method.BLOW,  '1/4'),
            Pitch(9, False,  Method.OVERDRAW,  '2b/4'),

            Pitch(10, False,  Method.DRAW,  '2/4'),
            Pitch(10, False,  Method.BLOW_BEND2,  '3b/4'),
            Pitch(10, False,  Method.BLOW_BEND1,  '3/4'),
            Pitch(10, False,  Method.BLOW,  '4/4'),
            Pitch(10, False,  Method.OVERDRAW,  '5b/4'),
        ]
    },
    'harmonic-minor' : {
        'description' : 'Lee Oskar harmonic minor',
        'scale' : [
            Pitch(1, False,  Method.BLOW,  '1/1'),
            Pitch(1, False,  Method.DRAW_BEND1,  '2b/1'),
            Pitch(1, False,  Method.DRAW,  '2/1'),
            Pitch(1, False,  Method.OVERBLOW,  '3b/1'),

            Pitch(2, False,  Method.BLOW,  '3b/1'),
            Pitch(2, False,  Method.DRAW_BEND3,  '3/1'),
            Pitch(2, False,  Method.DRAW_BEND2,  '4/1'),
            Pitch(2, False,  Method.DRAW_BEND1,  '4b/1'),
            Pitch(2, False,  Method.DRAW,  '5/1'),

            Pitch(3, False,  Method.BLOW,  '5/1'),
            Pitch(3, False,  Method.DRAW_BEND3,  '6b/1'),
            Pitch(3, False,  Method.DRAW_BEND2,  '6/1'),
            Pitch(3, False,  Method.DRAW_BEND1,  '7b/1'),
            Pitch(3, False,  Method.DRAW,  '7/1'),

            Pitch(4, False,  Method.BLOW,  '1/2'),
            Pitch(4, False,  Method.DRAW_BEND1,  '2b/2'),
            Pitch(4, False,  Method.DRAW,  '2/2'),
            Pitch(4, False,  Method.OVERBLOW,  '3b/2'),

            Pitch(5, False,  Method.BLOW,  '3b/2'),
            Pitch(5, False,  Method.DRAW_BEND1,  '3/1'),
            Pitch(5, False,  Method.DRAW,  '4/2'),
            Pitch(5, False,  Method.OVERBLOW,  '5b/2'),

            Pitch(6, False,  Method.BLOW,  '5/2'),
            Pitch(6, False,  Method.DRAW,  '6b/2'),
            Pitch(6, False,  Method.OVERBLOW,  '6/2'),
            # 7b ? Method.OVERBLOW2 -?
            Pitch(7, False,  Method.DRAW,  '7/2'),
            Pitch(7, False,  Method.BLOW,  '1/3'),

            Pitch(8, False,  Method.DRAW,  '2/3'),
            Pitch(8, False,  Method.BLOW,  '3b/3'),

            Pitch(9, False,  Method.DRAW,  '4/3'),
            Pitch(9, False,  Method.BLOW_BEND1,  '5b/3'),
            Pitch(9, False,  Method.BLOW,  '5/3'),
            Pitch(9, False,  Method.OVERDRAW,  '6b/3'),

            Pitch(10, False,  Method.DRAW,  '6b/3'),
            Pitch(10, False,  Method.BLOW_BEND3,  '6/3'),
            Pitch(10, False,  Method.BLOW_BEND2,  '7b/3'),
            Pitch(10, False,  Method.BLOW_BEND1,  '7/3'),
            Pitch(10, False,  Method.BLOW,  '1/4'),
            Pitch(10, False,  Method.OVERDRAW,  '2b/4'),
        ]
    },
    'wilde-tuned' : {
        'description' : 'Will Wilde tuning, Saydel harmonicas',
        'scale' : [
            # 1 - 5 the same as richter
            Pitch(1, False,  Method.BLOW,  '1/1'),
            Pitch(1, False,  Method.DRAW_BEND1,  '2b/1'),
            Pitch(1, False,  Method.DRAW,  '2/1'),
            Pitch(1, False,  Method.OVERBLOW,  '3b/1'),

            Pitch(2, False,  Method.BLOW,  '3/1'),
            Pitch(2, False,  Method.DRAW_BEND2,  '4/1'),
            Pitch(2, False,  Method.DRAW_BEND1,  '4b/1'),
            Pitch(2, False,  Method.DRAW,  '5/1'),

            Pitch(3, False,  Method.BLOW,  '5/1'),
            Pitch(3, False,  Method.DRAW_BEND3,  '6b/1'),
            Pitch(3, False,  Method.DRAW_BEND2,  '6/1'),
            Pitch(3, False,  Method.DRAW_BEND1,  '7b/1'),
            Pitch(3, False,  Method.DRAW,  '7/1'),

            Pitch(4, False,  Method.BLOW,  '1/2'),
            Pitch(4, False,  Method.DRAW_BEND1,  '2b/2'),
            Pitch(4, False,  Method.DRAW,  '2/2'),
            Pitch(4, False,  Method.OVERBLOW,  '3b/2'),

            Pitch(5, False,  Method.BLOW,  '3/2'),
            Pitch(5, False,  Method.DRAW,  '4/2'),

            # changed
            Pitch(6, False,  Method.BLOW,  '3/2'),
            Pitch(6, False,  Method.DRAW_BEND2,  '4/2'),
            Pitch(6, False,  Method.DRAW_BEND1,  '5b/2'),
            Pitch(6, False,  Method.DRAW,  '5/2'),
            Pitch(6, False,  Method.OVERBLOW,  '6b/2'),

            Pitch(7, False,  Method.BLOW,  '5/2'),
            Pitch(7, False,  Method.DRAW_BEND3,  '6b/2'),
            Pitch(7, False,  Method.DRAW_BEND2,  '6/2'),
            Pitch(7, False,  Method.DRAW_BEND1,  '7b/2'),
            Pitch(7, False,  Method.DRAW,  '7/2'),

            Pitch(8, False,  Method.BLOW,  '1/3'),
            Pitch(8, False,  Method.DRAW_BEND1,  '2b/3'),
            Pitch(8, False,  Method.DRAW,  '2/3'),

            Pitch(9, False,  Method.BLOW,  '3/3'),
            Pitch(9, False,  Method.DRAW_BEND2,  '4/3'),
            Pitch(9, False,  Method.DRAW_BEND1,  '5b/3'),
            Pitch(9, False,  Method.DRAW,  '5/3'),
            Pitch(9, False,  Method.OVERBLOW,  '6b/3'),

            Pitch(10, False,  Method.BLOW,  '6/3'),
            Pitch(10, False,  Method.DRAW_BEND2,  '7b/3'),
            Pitch(10, False,  Method.DRAW_BEND1,  '7/3'),
            Pitch(10, False,  Method.DRAW,  '1/4'),
            Pitch(10, False,  Method.OVERBLOW,  '2b/4'),
        ]
    },
    'chromatic': {
        'description' : 'chromatic with 3 octaves',
        'scale' : [
            Pitch(1, False,  Method.BLOW,  '1/1'),
            Pitch(1, False,  Method.DRAW_BEND1,  '2b/1'),
            Pitch(1, False,  Method.DRAW,  '2/1'),

            Pitch(1, True,  Method.BLOW,  '2b/1'),
            Pitch(1, True,  Method.DRAW_BEND1,  '2/1'),
            Pitch(1, True,  Method.DRAW,  '3b/1'),

            Pitch(2, False,  Method.BLOW,  '3/1'),
            Pitch(2, False,  Method.DRAW,  '4/1'),

            Pitch(2, True,  Method.BLOW,  '4/1'),
            Pitch(2, True,  Method.DRAW,  '5b/1'),

            Pitch(3, False,  Method.BLOW,  '5/1'),
            Pitch(3, False,  Method.DRAW_BEND1,  '6b/1'),
            Pitch(3, False,  Method.DRAW,  '6/1'),

            Pitch(3, True,  Method.BLOW, '6b/1'),
            Pitch(3, True,  Method.DRAW_BEND1, '6/1'),
            Pitch(3, True,  Method.DRAW, '7b/1'),

            Pitch(4, False,  Method.DRAW,  '7/1'),
            Pitch(4, False,  Method.BLOW,  '1/2'),

            Pitch(4, True,  Method.DRAW,  '1/2'),
            Pitch(4, True,  Method.BLOW,  '2b/2'),

            Pitch(5, False,  Method.BLOW,  '1/2'),
            Pitch(5, False,  Method.DRAW_BEND1,  '2b/2'),
            Pitch(5, False,  Method.DRAW,  '2/2'),

            Pitch(5, True,  Method.BLOW,  '2b/2'),
            Pitch(5, True,  Method.DRAW_BEND1,  '2/2'),
            Pitch(5, True,  Method.DRAW,  '3b/2'),

            Pitch(6, False,  Method.BLOW,  '3/2'),
            Pitch(6, False,  Method.DRAW,  '4/2'),

            Pitch(6, True,  Method.BLOW,  '4/2'),
            Pitch(6, True,  Method.DRAW,  '5b/2'),

            Pitch(7, False,  Method.BLOW,  '5/2'),
            Pitch(7, False,  Method.DRAW_BEND1,  '6b/2'),
            Pitch(7, False,  Method.DRAW,  '6/2'),

            Pitch(7, True,  Method.BLOW,  '6b/2'),
            Pitch(7, True,  Method.DRAW_BEND1,  '6/2'),
            Pitch(7, True,  Method.DRAW,  '7b/2'),

            Pitch(8, False,  Method.DRAW,  '7/2'),
            Pitch(8, False,  Method.BLOW,  '1/3'),

            Pitch(8, True,  Method.DRAW,  '1/3'),
            Pitch(8, True,  Method.BLOW,  '2b/3'),

            Pitch(9, False,  Method.BLOW,  '1/3'),
            Pitch(9, False,  Method.DRAW_BEND1,  '2b/3'),
            Pitch(9, False,  Method.DRAW,  '2/3'),

            Pitch(9, True,  Method.BLOW,  '2b/3'),
            Pitch(9, True,  Method.DRAW_BEND1,  '2/3'),
            Pitch(9, True,  Method.DRAW,  '3b/3'),

            Pitch(10, False,  Method.BLOW,  '3/3'),
            Pitch(10, False,  Method.DRAW,  '4/3'),

            Pitch(10, True,  Method.BLOW,  '4/3'),
            Pitch(10, True,  Method.DRAW,  '5b/3'),

            Pitch(11, False,  Method.BLOW,  '5/3'),
            Pitch(11, False,  Method.DRAW_BEND1,  '6b/3'),
            Pitch(11, False,  Method.DRAW,  '6/3'),

            Pitch(11, True,  Method.BLOW,  '6b/3'),
            Pitch(11, True,  Method.DRAW_BEND1,  '6/3'),
            Pitch(11, True,  Method.DRAW,  '7b/3'),

            Pitch(12, False,  Method.DRAW,  '7/3'),
            Pitch(12, False,  Method.BLOW,  '1/4'),

            Pitch(12, True,  Method.DRAW,  '1/4'),
            Pitch(12, True,  Method.BLOW,  '2b/4'),
        ]
    },
    'trochilus-pop' : {
        'description': 'JDR harmonica Trochilus pop tuning',
        'scale' : [
            Pitch(1, False,  Method.BLOW,  '1/1'),
            Pitch(1, False,  Method.DRAW_BEND1,  '2b/1'),
            Pitch(1, False,  Method.DRAW,  '2/1'),

            Pitch(1, True,  Method.BLOW,  '2b/1'),
            Pitch(1, True,  Method.DRAW_BEND1,  '2/1'),
            Pitch(1, True,  Method.DRAW,  '3b/1'),

            Pitch(2, False,  Method.BLOW,  '3/1'),
            Pitch(2, False,  Method.DRAW_BEND2,  '4/1'),
            Pitch(2, False,  Method.DRAW_BEND1,  '5b/1'),
            Pitch(2, False,  Method.DRAW,  '5/1'),

            Pitch(2, True,  Method.BLOW,  '4/1'),
            Pitch(2, True,  Method.DRAW,  '5b/1'),

            Pitch(3, False,  Method.BLOW,  '6/1'),
            Pitch(3, False,  Method.DRAW_BEND1,  '7b/1'),
            Pitch(3, False,  Method.DRAW,  '7/1'),

            Pitch(3, True,  Method.DRAW,  '6b/1'),
            Pitch(3, True,  Method.BLOW_BEND1,  '6/1'), # blow!
            Pitch(3, True,  Method.BLOW,  '7b/1'),

            Pitch(4, False,  Method.BLOW,  '1/2'),
            Pitch(4, False,  Method.DRAW_BEND1,  '2b/2'),
            Pitch(4, False,  Method.DRAW,  '2/2'),

            Pitch(4, True,  Method.BLOW,  '2b/2'),
            Pitch(4, True,  Method.DRAW_BEND1,  '2/2'),
            Pitch(4, True,  Method.DRAW,  '3b/2'),

            Pitch(5, False,  Method.BLOW,  '3/2'),
            Pitch(5, False,  Method.DRAW,  '4/2'),

            Pitch(5, True,  Method.BLOW,  '4/2'),
            Pitch(5, True,  Method.DRAW,  '5b/2'),

            Pitch(6, False,  Method.BLOW,  '5/2'),
            Pitch(6, False,  Method.DRAW_BEND1,  '6b/2'),
            Pitch(6, False,  Method.DRAW,  '6/2'),

            Pitch(6, True,  Method.BLOW,  '6b/2'),
            Pitch(6, True,  Method.DRAW_BEND1,  '6/2'),
            Pitch(6, True,  Method.DRAW,  '7b/2'),

            Pitch(7, False,  Method.DRAW,  '7/2'),
            Pitch(7, False,  Method.BLOW,  '1/3'),

            Pitch(7, True,  Method.DRAW,  '1/3'),
            Pitch(7, True,  Method.BLOW,  '2b/3'),

            Pitch(8, False,  Method.DRAW,  '2/3'),
            Pitch(8, False,  Method.BLOW_BEND1,  '3b/3'),
            Pitch(8, False,  Method.BLOW,  '3/3'),

            Pitch(8, True,  Method.DRAW,  '3b/3'),
            Pitch(8, True,  Method.BLOW_BEND1,  '3/3'),
            Pitch(8, True,  Method.BLOW,  '4/3'),

            Pitch(9, False,  Method.DRAW,  '4/3'),
            Pitch(9, False,  Method.BLOW_BEND1,  '5b/3'),
            Pitch(9, False,  Method.BLOW,  '5/3'),

            Pitch(9, True,  Method.DRAW,  '5b/3'),
            Pitch(9, True,  Method.BLOW_BEND1,  '5/3'),
            Pitch(9, True,  Method.BLOW,  '6b/3'),

            Pitch(10, False,  Method.DRAW,  '6/3'),
            Pitch(10, False,  Method.BLOW_BEND2,  '7b/3'),
            Pitch(10, False,  Method.BLOW_BEND1,  '7/3'),
            Pitch(10, False,  Method.BLOW,  '1/4'),

            Pitch(10, True,  Method.DRAW,  '7b/3'),
            Pitch(10, True,  Method.BLOW,  '7/3'),
        ]
    }
}

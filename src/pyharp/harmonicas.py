import enum
from collections import namedtuple

@enum.unique
class Method(enum.Enum):
    BLOW = 0
    DRAW = 1
    DRAW_BEND1 = 2
    DRAW_BEND2 = 3
    DRAW_BEND3 = 4
    BLOW_BEND1 = 5
    BLOW_BEND2 = 6
    OVERBLOW = 7
    OVERDRAW = 8
    

Pitch = namedtuple('Pitch', ['hole', 'pitch',  'method'])

harmonicas = {
    'richter' : {
        'description':'',
        'scale' : [
            Pitch(1, '1/1', Method.BLOW),
            Pitch(1, '2b/1', Method.DRAW_BEND1),
            Pitch(1, '2/1', Method.DRAW),
            Pitch(1, '3b/1', Method.OVERBLOW),

            Pitch(2, '3/1', Method.BLOW),
            Pitch(2, '4/1', Method.DRAW_BEND2),
            Pitch(2, '4b/1', Method.DRAW_BEND1),
            Pitch(2, '5/1', Method.DRAW),

            Pitch(3, '5/1', Method.BLOW),
            Pitch(3, '6b/1', Method.DRAW_BEND3),
            Pitch(3, '6/1', Method.DRAW_BEND2),
            Pitch(3, '7b/1', Method.DRAW_BEND1),
            Pitch(3, '7/1', Method.DRAW),

            Pitch(4, '1/2', Method.BLOW),
            Pitch(4, '2b/2', Method.DRAW_BEND1),
            Pitch(4, '2/2', Method.DRAW),
            Pitch(4, '3b/2', Method.OVERBLOW),

            Pitch(5, '3/2', Method.BLOW),
            Pitch(5, '4/2', Method.DRAW),
            Pitch(5, '5b/2', Method.OVERBLOW),

            Pitch(6, '5/2', Method.BLOW),
            Pitch(6, '6b/2', Method.DRAW_BEND1),
            Pitch(6, '6/2', Method.DRAW),
            Pitch(6, '7b/2', Method.OVERBLOW),

            Pitch(7, '7/2', Method.DRAW),
            Pitch(7, '1/3', Method.BLOW),

            Pitch(8, '2/3', Method.DRAW),
            Pitch(8, '3b/3', Method.BLOW_BEND1),
            Pitch(8, '3/3', Method.BLOW),

            Pitch(9, '4/3', Method.DRAW),
            Pitch(9, '5b/3', Method.BLOW_BEND1),
            Pitch(9, '5/3', Method.BLOW),
            Pitch(9, '6b/3', Method.OVERDRAW),

            Pitch(10, '6/3', Method.DRAW),
            Pitch(10, '7b/3', Method.BLOW_BEND2),
            Pitch(10, '7/3', Method.BLOW_BEND1),
            Pitch(10, '1/4', Method.BLOW),
            Pitch(10, '2b/4', Method.OVERDRAW),
        ],
    },
    'paddy-richter' : {
        'description':'a Brendan Power tuning',
        'scale' : [
            Pitch(1, '1/1', Method.BLOW),
            Pitch(1, '2b/1', Method.DRAW_BEND1),
            Pitch(1, '2/1', Method.DRAW),
            Pitch(1, '3b/1', Method.OVERBLOW),

            Pitch(2, '3/1', Method.BLOW),
            Pitch(2, '4/1', Method.DRAW_BEND2),
            Pitch(2, '4b/1', Method.DRAW_BEND1),
            Pitch(2, '5/1', Method.DRAW),

            Pitch(3, '6/1', Method.BLOW),
            Pitch(3, '7b/1', Method.DRAW_BEND1),
            Pitch(3, '7/1', Method.DRAW),

            Pitch(4, '1/2', Method.BLOW),
            Pitch(4, '2b/2', Method.DRAW_BEND1),
            Pitch(4, '2/2', Method.DRAW),
            Pitch(4, '3b/2', Method.OVERBLOW),

            Pitch(5, '3/2', Method.BLOW),
            Pitch(5, '4/2', Method.DRAW),
            Pitch(5, '5b/2', Method.OVERBLOW),

            Pitch(6, '5/2', Method.BLOW),
            Pitch(6, '6b/2', Method.DRAW_BEND1),
            Pitch(6, '6/2', Method.DRAW),
            Pitch(6, '7b/2', Method.OVERBLOW),

            Pitch(7, '7/2', Method.DRAW),
            Pitch(7, '1/3', Method.BLOW),

            Pitch(8, '2/3', Method.DRAW),
            Pitch(8, '3b/3', Method.BLOW_BEND1),
            Pitch(8, '3/3', Method.BLOW),

            Pitch(9, '4/3', Method.DRAW),
            Pitch(9, '5b/3', Method.BLOW_BEND1),
            Pitch(9, '5/3', Method.BLOW),
            Pitch(9, '6b/3', Method.OVERDRAW),

            Pitch(10, '6/3', Method.DRAW),
            Pitch(10, '7b/3', Method.BLOW_BEND2),
            Pitch(10, '7/3', Method.BLOW_BEND1),
            Pitch(10, '1/4', Method.BLOW),
            Pitch(10, '2b/4', Method.OVERDRAW),
        ],
    },
    'power-bender' : {
        'description':'a Brendan Power tuning',
        'scale': [
            # as in Richer
            Pitch(1, '1/1', Method.BLOW),
            Pitch(1, '2b/1', Method.DRAW_BEND1),
            Pitch(1, '2/1', Method.DRAW),
            Pitch(1, '3b/1', Method.OVERBLOW),

            Pitch(2, '3/1', Method.BLOW),
            Pitch(2, '4/1', Method.DRAW_BEND2),
            Pitch(2, '4b/1', Method.DRAW_BEND1),
            Pitch(2, '5/1', Method.DRAW),

            Pitch(3, '5/1', Method.BLOW),
            Pitch(3, '6b/1', Method.DRAW_BEND3),
            Pitch(3, '6/1', Method.DRAW_BEND2),
            Pitch(3, '7b/1', Method.DRAW_BEND1),
            Pitch(3, '7/1', Method.DRAW),

            Pitch(4, '1/2', Method.BLOW),
            Pitch(4, '2b/2', Method.DRAW_BEND1),
            Pitch(4, '2/2', Method.DRAW),
            Pitch(4, '3b/2', Method.OVERBLOW),
            # changed pitches
            Pitch(5, '2/2', Method.BLOW),
            Pitch(4, '3b/2', Method.DRAW_BEND1),
            Pitch(5, '3/2', Method.DRAW),

            Pitch(6, '4/2', Method.BLOW),
            Pitch(6, '5b/2', Method.DRAW_BEND1),
            Pitch(6, '5/2', Method.DRAW),
            Pitch(6, '6b/2', Method.OVERBLOW),

            Pitch(7, '6/2', Method.BLOW),
            Pitch(6, '7b/2', Method.DRAW_BEND1),
            Pitch(7, '7/2', Method.DRAW),

            Pitch(8, '1/3', Method.BLOW),
            Pitch(8, '2b/3', Method.DRAW_BEND1),
            Pitch(8, '2/3', Method.DRAW),

            Pitch(9, '3/3', Method.BLOW),
            Pitch(9, '5b/3', Method.BLOW_BEND1),
            Pitch(9, '5/3', Method.DRAW),
            Pitch(9, '6b/3', Method.OVERDRAW),

            Pitch(10, '6/3', Method.BLOW),
            Pitch(10, '7b/3', Method.DRAW_BEND2),
            Pitch(10, '7/3', Method.DRAW_BEND1),
            Pitch(10, '1/4', Method.DRAW),
            Pitch(10, '2b/4', Method.OVERBLOW),
        ]
    },
    'melody-maker' : {
        'description':'Lee Oskar (Tombo) harmonicas',
        'scale': [
            Pitch(1, '4/1', Method.BLOW),
            Pitch(1, '5b/1', Method.DRAW_BEND1),
            Pitch(1, '5/1', Method.DRAW),

            Pitch(2, '6/1', Method.BLOW),
            Pitch(2, '7b/1', Method.DRAW_BEND2),
            Pitch(2, '7/1', Method.DRAW_BEND1),
            Pitch(2, '1/2', Method.DRAW),

            Pitch(3, '2/2', Method.BLOW),
            Pitch(3, '3b/2', Method.DRAW_BEND1),
            Pitch(3, '3/2', Method.DRAW),

            Pitch(4, '4/3', Method.BLOW),
            Pitch(4, '5b/3', Method.DRAW_BEND1),
            Pitch(4, '5/3', Method.DRAW),

            Pitch(5, '6/3', Method.BLOW),
            Pitch(4, '7b/3', Method.DRAW_BEND1),
            Pitch(5, '7/3', Method.DRAW),

            Pitch(6, '1/3', Method.BLOW),
            Pitch(6, '2b/3', Method.DRAW_BEND1),
            Pitch(6, '2/3', Method.DRAW),

            Pitch(7, '3/3', Method.DRAW),
            Pitch(7, '4/3', Method.BLOW),

            Pitch(8, '5/3', Method.DRAW),
            Pitch(8, '6b/3', Method.BLOW_BEND1),
            Pitch(8, '6/3', Method.BLOW),

            Pitch(9, '7/3', Method.DRAW),
            Pitch(9, '1/4', Method.BLOW),

            Pitch(10, '2/4', Method.DRAW),
            Pitch(10, '3b/4', Method.BLOW_BEND2),
            Pitch(10, '3/4', Method.BLOW_BEND1),
            Pitch(10, '4/4', Method.BLOW),
        ]
    },
    'penta-harp' : {
        'description':'Hohner Penta Harp - minor pentatonic tuning',
        'scale': [
            Pitch(1, '1/1', Method.BLOW),
            Pitch(1, '2b/1', Method.DRAW_BEND2),
            Pitch(1, '2/1', Method.DRAW_BEND1),
            Pitch(1, '3b/1', Method.DRAW),
            Pitch(1, '3/1', Method.OVERBLOW),
    
            Pitch(2, '4/1', Method.BLOW),
            Pitch(2, '5b/1', Method.DRAW),
            
            Pitch(3, '5/1', Method.BLOW),
            Pitch(3, '6b/1', Method.DRAW_BEND2),
            Pitch(3, '6/1', Method.DRAW_BEND1),
            Pitch(3, '7b/1', Method.DRAW),
            Pitch(3, '7/1', Method.OVERBLOW),
            
            Pitch(4, '1/2', Method.BLOW),
            Pitch(4, '2b/2', Method.DRAW_BEND2),
            Pitch(4, '2/2', Method.DRAW_BEND1),
            Pitch(4, '3b/2', Method.DRAW),
            Pitch(4, '3/2', Method.OVERBLOW),

            Pitch(5, '4/2', Method.BLOW),
            Pitch(5, '5b/2', Method.DRAW),
            
            Pitch(6, '5/2', Method.BLOW),
            Pitch(6, '6b/2', Method.DRAW_BEND2),
            Pitch(6, '6/2', Method.DRAW_BEND1),
            Pitch(6, '7b/2', Method.DRAW),
            Pitch(6, '7/2', Method.OVERBLOW),
            
            Pitch(7, '1/3', Method.BLOW),
            Pitch(7, '2b/3', Method.DRAW_BEND2),
            Pitch(7, '2/3', Method.DRAW_BEND1),
            Pitch(7, '3b/3', Method.DRAW),
            Pitch(7, '3/3', Method.OVERBLOW),

            Pitch(8, '4/3', Method.BLOW),
            Pitch(8, '5b/3', Method.DRAW),
            
            Pitch(9, '5/3', Method.BLOW),
            Pitch(9, '6b/3', Method.DRAW_BEND2),
            Pitch(9, '6/3', Method.DRAW_BEND1),
            Pitch(9, '7b/3', Method.DRAW),
            Pitch(9, '7/3', Method.OVERBLOW),
            
            Pitch(10, '1/4', Method.BLOW),
            Pitch(10, '2b/4', Method.DRAW_BEND2),
            Pitch(10, '2/4', Method.DRAW_BEND1),
            Pitch(10, '3b/4', Method.DRAW),
            Pitch(10, '3/4', Method.OVERBLOW),
        ],
    },
    'major-cross' : {
        'description': 'Seydel Major Cross Tuning',
        'scale': [
            Pitch(1, '5/0', Method.BLOW),
            Pitch(1, '6b/0', Method.DRAW_BEND1),
            Pitch(1, '6/0', Method.DRAW),
            Pitch(1, '7b/0', Method.OVERBLOW),

            Pitch(2, '7/0', Method.BLOW),
            Pitch(2, '1/1', Method.DRAW),
            Pitch(1, '2b/1', Method.OVERBLOW),

            Pitch(3, '2/1', Method.BLOW),
            Pitch(3, '3b/1', Method.DRAW_BEND1),
            Pitch(3, '3/1', Method.DRAW),

            Pitch(4, '4/1', Method.BLOW),
            Pitch(4, '5b/1', Method.DRAW_BEND1),
            Pitch(4, '5/1', Method.DRAW),
            Pitch(4, '6b/1', Method.OVERBLOW),

            Pitch(5, '6/1', Method.BLOW),
            Pitch(4, '7b/1', Method.DRAW_BEND1),
            Pitch(5, '7/1', Method.DRAW),

            Pitch(6, '1/2', Method.BLOW),
            Pitch(6, '2b/2', Method.DRAW_BEND1),
            Pitch(6, '2/2', Method.DRAW),
            Pitch(6, '3b/2', Method.OVERBLOW),

            Pitch(7, '3/2', Method.DRAW),
            Pitch(7, '4/2', Method.BLOW),
            Pitch(7, '5b/2', Method.OVERDRAW),

            Pitch(8, '5/2', Method.DRAW),
            Pitch(8, '6b/2', Method.BLOW_BEND1),
            Pitch(8, '6/2', Method.BLOW),
            Pitch(8, '7b/2', Method.OVERDRAW),

            Pitch(9, '7/2', Method.DRAW),
            Pitch(9, '1/3', Method.BLOW),
            Pitch(9, '2b/3', Method.OVERDRAW),

            Pitch(10, '2/3', Method.DRAW),
            Pitch(10, '3b/3', Method.BLOW_BEND1),
            Pitch(10, '3/3', Method.BLOW),
            Pitch(10, '4/3', Method.OVERDRAW),
        ],
    },
    'penta-harp': {
        'description': 'Hohner Penta Harp',
        'scale' : [
            Pitch(1, '1/1', Method.BLOW),
            Pitch(1, '2b/1', Method.DRAW_BEND2),
            Pitch(1, '2/1', Method.DRAW_BEND1),
            Pitch(1, '3b/1', Method.DRAW),
            Pitch(1, '3/1', Method.OVERBLOW),

            Pitch(2, '4/1', Method.BLOW),
            Pitch(2, '5b/1', Method.DRAW),

            Pitch(3, '5/1', Method.BLOW),
            Pitch(3, '6b/1', Method.DRAW_BEND2),
            Pitch(3, '6/1', Method.DRAW_BEND1),
            Pitch(3, '7b/1', Method.DRAW),
            Pitch(3, '7/1', Method.OVERBLOW),

            Pitch(4, '1/2', Method.BLOW),
            Pitch(4, '2b/2', Method.DRAW_BEND2),
            Pitch(4, '2/2', Method.DRAW_BEND1),
            Pitch(4, '3b/2', Method.DRAW),
            Pitch(4, '3/2', Method.OVERBLOW),

            Pitch(2, '4/2', Method.BLOW),
            Pitch(2, '5b/2', Method.DRAW),

            Pitch(6, '5/2', Method.BLOW),
            Pitch(6, '6b/2', Method.DRAW_BEND2),
            Pitch(6, '6/2', Method.DRAW_BEND1),
            Pitch(6, '7b/2', Method.DRAW),
            Pitch(6, '7/2', Method.OVERBLOW),

            Pitch(7, '1/3', Method.BLOW),
            Pitch(7, '2b/3', Method.DRAW_BEND2),
            Pitch(7, '2/3', Method.DRAW_BEND1),
            Pitch(7, '3b/3', Method.DRAW),
            Pitch(7, '3/3', Method.OVERBLOW),

            Pitch(8, '4/3', Method.BLOW),
            Pitch(8, '5b/3', Method.DRAW),

            Pitch(9, '5/3', Method.BLOW),
            Pitch(9, '6b/3', Method.BLOW_BEND2),
            Pitch(9, '6/3', Method.BLOW_BEND1),
            Pitch(9, '7b/3', Method.DRAW),
            Pitch(9, '7/3', Method.OVERBLOW),

            Pitch(4, '1/4', Method.BLOW),
            Pitch(4, '2b/4', Method.DRAW_BEND2),
            Pitch(4, '2/4', Method.DRAW_BEND1),
            Pitch(4, '3b/4', Method.DRAW),
            Pitch(4, '3/4', Method.OVERBLOW),
        ],        
    },
    'orchestra-s': {
        'description': 'Saydel Orchestra-S',
        'scale': [
            Pitch(1, '5/1', Method.BLOW),
            Pitch(1, '6b/1', Method.DRAW_BEND1),
            Pitch(1, '6/1', Method.DRAW),
            Pitch(1, '7b/1', Method.OVERBLOW),

            Pitch(2, '7/1', Method.DRAW),
            Pitch(2, '1/2', Method.BLOW),

            Pitch(3, '1/2', Method.BLOW),
            Pitch(3, '2b/2', Method.DRAW_BEND1),
            Pitch(3, '2/2', Method.DRAW),
            Pitch(3, '3b/2', Method.OVERBLOW),

            Pitch(4, '3/2', Method.BLOW),
            Pitch(4, '4/2', Method.DRAW),
            Pitch(4, '5b/2', Method.OVERBLOW),

            Pitch(5, '5/2', Method.BLOW),
            Pitch(5, '6b/2', Method.DRAW_BEND1),
            Pitch(5, '6/2', Method.DRAW),
            Pitch(5, '7b/2', Method.OVERBLOW),

            Pitch(6, '7/2', Method.DRAW),
            Pitch(6, '1/3', Method.BLOW),

            Pitch(7, '1/3', Method.BLOW),
            Pitch(7, '2b/3', Method.DRAW_BEND1),
            Pitch(7, '2/3', Method.DRAW),
            Pitch(7, '3b/3', Method.OVERBLOW),

            Pitch(8, '3/3', Method.BLOW),
            Pitch(8, '4/3', Method.DRAW),
            Pitch(8, '5b/3', Method.OVERBLOW),

            Pitch(9, '5/3', Method.BLOW),
            Pitch(9, '6b/3', Method.DRAW_BEND1),
            Pitch(9, '6/3', Method.DRAW),
            Pitch(9, '7b/3', Method.OVERBLOW),

            Pitch(10, '7/3', Method.DRAW),
            Pitch(10, '1/4', Method.BLOW),

        ]
    },
    'solist-pro': {
        'description': 'Saydel Solist Pro (12 hole)',
        'scale': [
            Pitch(1, '1/1', Method.BLOW),
            Pitch(1, '2b/1', Method.DRAW_BEND1),
            Pitch(1, '2/1', Method.DRAW),
            Pitch(1, '3b/1', Method.OVERBLOW),

            Pitch(2, '3/1', Method.BLOW),
            Pitch(2, '4/1', Method.DRAW),
            Pitch(2, '5b/1', Method.OVERBLOW),

            Pitch(3, '5/1', Method.BLOW),
            Pitch(3, '6b/1', Method.DRAW_BEND1),
            Pitch(3, '6/1', Method.DRAW),
            Pitch(3, '7b/1', Method.OVERBLOW),

            Pitch(4, '7/1', Method.DRAW),
            Pitch(4, '1/2', Method.BLOW),

            Pitch(5, '1/2', Method.BLOW),
            Pitch(5, '2b/2', Method.DRAW_BEND1),
            Pitch(5, '2/2', Method.DRAW),
            Pitch(5, '3b/2', Method.OVERBLOW),

            Pitch(6, '3/2', Method.BLOW),
            Pitch(6, '4/2', Method.DRAW),
            Pitch(6, '5b/2', Method.OVERBLOW),

            Pitch(7, '5/2', Method.BLOW),
            Pitch(7, '6b/2', Method.DRAW_BEND1),
            Pitch(7, '6/2', Method.DRAW),
            Pitch(7, '7b/2', Method.OVERBLOW),

            Pitch(8, '7/2', Method.DRAW),
            Pitch(8, '1/3', Method.BLOW),

            Pitch(9, '1/3', Method.BLOW),
            Pitch(9, '2b/3', Method.DRAW_BEND1),
            Pitch(9, '2/3', Method.DRAW),
            Pitch(9, '3b/3', Method.OVERBLOW),

            Pitch(10, '3/3', Method.BLOW),
            Pitch(10, '4/3', Method.DRAW),
            Pitch(10, '5b/3', Method.OVERBLOW),

            Pitch(11, '5/3', Method.BLOW),
            Pitch(11, '6b/3', Method.DRAW_BEND1),
            Pitch(11, '6/3', Method.DRAW),
            Pitch(11, '7b/3', Method.OVERBLOW),

            Pitch(12, '7/3', Method.DRAW),
            Pitch(12, '1/4', Method.BLOW),
        ]
    },
}

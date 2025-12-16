from __future__ import annotations # for list annotations
from typing import Mapping, Union, Optional, TypeAlias, Set

# from dataclasses import dataclass

chord_meanings = {
    # Triades
    '' : ('1','3','5'),
    'maj' : ('1','3','5'),
    'M' : ('1','3','5'),
    'm' : ('1','3b','5'),
    'min' : ('1','3b','5'),
    '-' : ('1','3b','5'),
    'aug' : ('1','3','5#'),
    '+' : ('1','3','5#'),
    'dim' : ('1','3b','5b'),
    'o' : ('1','3b','5b'),

    # Seventh chords
    '7' : ('1','3','5','7b'),
    'maj7' : ('1','3','5','7'),
    'M7' : ('1','3','5','7'),
    'minmaj7' : ('1','3b','5','7'),
    'mM7' : ('1','3b','5','7'),
    '-M7' : ('1','3b','5','7'),
    'm7' : ('1','3b','5','7b'),
    'min7' : ('1','3b','5','7b'),
    '-7' : ('1','3b','5','7b'), #
    'augmaj7' : ('1','3','5#','7'),
    '+M7' : ('1','3','5#','7'),
    'aug7' : ('1','3','5#','7b'),
    '+7' : ('1','3','5#','7b'),  #aug7
    'dim7' : ('1','3b','5b','6'),
    'o7' : ('1','3b','5b','6'),
    'min7dim5' : ('1','3b','5b','7b'), # half-diminished
    'x7' : ('1','3b','5b','7b'), # half-diminished - can use a better symbol?
    '7dim5' : ('1','3','5b','7b'), #
    '7b5' : ('1','3','5b','7b'), #

    # Ninth chords
    'maj9' : ('1','3','5','7','9'),
    'M9' : ('1','3','5','7','9'),

    '9' : ('1','3','5','7b','9'),
    '7b9': ('1','3','5','7b','9b'),

    'minmaj9' : ('1','3b','5','7','9'),
    'mM9' : ('1','3b','5','7','9'),
    '-M9' : ('1','3b','5','7','9'),

    'm9' : ('1','3b','5','7b','9'),
    'min9' : ('1','3b','5','7b','9'),
    '-9' : ('1','3b','5','7b','9'),

    'augmaj9' : ('1','3','5#','7','9'),
    '+M9' : ('1','3','5#','7','9'),

    'aug9' : ('1','3','5#','7b','9'),
    '+9' : ('1','3','5#','7b','9'),
    '9#5' : ('1','3','5#','7b','9'),

    'x9' :  ('1','3b','5b','7b','9'), # half-diminished
    'xb9' :  ('1','3b','5b','7b','9b'), # half-diminished minor ninth

    'dim9' :  ('1','3b','5b','6','9'), # Diminished ninth
    'o9' :  ('1','3b','5b','6','9'), # Diminished ninth
    'dimb9' :  ('1','3b','5b','6','9b'), # Diminished minor ninth
    'ob9' :  ('1','3b','5b','6','9b'), # Diminished minor ninth

    # Eleventh chords
    # TODO: alterations of 11
    '11' : ('1','3','5','7b','9','11'),

    'maj11' : ('1','3','5','7','9','11'),
    'M11' : ('1','3','5','7','9','11'),

    'm11' : ('1','3b','5','7','9','11'),
    'min11' : ('1','3b','5','7','9','11'),
    '-11' : ('1','3b','5','7','9','11'),

    'augmaj11' : ('1','3','5#','7','9','11'),
    '+M11' : ('1','3','5#','7','9','11'),

    'aug11' :  ('1','3','5#','7b','9','11'),
    'x11' : ('1','3b','5b','7b','9','11'), # Half-diminished eleventh
    'dim11' : ('1','3b','5b','6','9','11'), # diminished eleventh

    # Thirteenth chords
    # TODO: alterations
    'maj13' : ('1','3','5','7','11','13'),
    'm13' : ('1','3b','5','7b','11','13'),
    '13' : ('1','3','5','7b','11','13'),

    #
    '6' : ('1','3','5','6'),
    'm6' : ('1','3b','5','6'),
    #
    # sus
    # TODO: add this to the parser
    'sus2' : ('1','2','5'),
    'sus4' : ('1','4','5'),
    'sus' : ('1','4','5'),
}

def parse_chord(chord : str):
    chord_and_bass = chord.strip().split('/')
    chord = chord_and_bass[0]
    bass_part = chord_and_bass[1] if len(chord_and_bass) > 1 else None

    if len(chord) > 1 and chord[1] in ['#', 'b']:
        key = chord[0:2].lower()
        meaning = chord[2:]
    else:
        key = chord[0].lower()
        meaning = ''

    scale = chord_meanings.get(meaning, ())
    bass = bass_part.lower() if bass_part is not None else key
    return key,bass,scale

from collections import namedtuple

Score_Pitch = namedtuple('Score_Pitch', ['step', 'octave', 'interval'])

intervals = {
    '1b': -1,
    '1': 0,
    '1#': 1,
    '2b': 1,
    '2': 2,
    '2#': 3,
    '3b': 3,
    '3': 4,
    '4b': 4,
    '3#': 5,
    '4': 5,
    '4#': 6,
    '5b': 6,
    '5': 7,
    '5#': 8,
    '6b': 8,
    '6':9,
    '6#': 10,
    '7b': 10,
    '7': 11,
    '8b': 11,
    '7#': 12,
    '8': 12,
}


def split_note(str):
    pitch_pair = str.split('/') # octave delimiter
    step = pitch_pair[0]
    octave = int(pitch_pair[1]) if len(pitch_pair) > 1 else 0
    return step, octave


def score_minus(p1,p2):
    pass

def parse_score(score_str):
    print(score_str)
    score = score_str.split(',')
    print(score)

    result = []

    for p in score:
        step, octave = split_note(p)
        interval = intervals[step]
        octave = 1 if octave == 0 else octave
        result.append(Score_Pitch(step, octave, interval))

    print(result)

from collections import namedtuple
from scale import scale_pitch, find_pitch, note_pitch

class WrongScorePitch(Exception):
    def __init__(self, pitch): self.pitch = pitch
    def __str__ (self): return 'Wrong pitch symbol'

ScorePitch = namedtuple('Score_Pitch', ['step', 'octave', 'interval'])


def parse_pitch(score):
    pitch_pair = score.strip().split('/') # octave delimiter
    try:
        step_part = pitch_pair[0]
        step = int(step_part[0])
        alter_char = step_part[1].lower() if len(step_part) > 1 else None
        octave = int(pitch_pair[1]) if len(pitch_pair) > 1 else 1
        interval = scale_pitch(step)[1] + (octave - 1) * 12
        interval_alt = interval+1 if alter_char == '#' else (interval-1 if alter_char == 'b' else interval)
    except Exception as e:
        print(e)
        raise WrongScorePitch(str)

    return ScorePitch(step_part, 1 if octave == 0 else octave, interval_alt)

def parse_note(score):
    pitch_pair = score.strip().split('/') # octave delimiter
    try:
        step_part = pitch_pair[0]
        letter = step_part[0].lower()
        alter_char = step_part[1] if len(step_part) > 1 else None

        index = -1
        for i,p in enumerate(MAJOR_SCALE):
            if p[0] == letter:
                index = i
                break
        if index < 0: raise WrongScorePitch(str)

        step = index + 1
        step_str = str(step) + (alter_char if alter_char else '')
        octave = int(pitch_pair[1]) if len(pitch_pair) > 1 else 1
        interval = MAJOR_SCALE[index][1] + (octave - 1) * 12
        interval_alt = interval+1 if alter_char == '#' else (interval-1 if alter_char == 'b' else interval)
    except Exception as e:
        print(e)
        raise WrongScorePitch(str)

    return ScorePitch(step_str, 1 if octave == 0 else octave, interval_alt)


def pitch_minus(p1,p2):
    pass

def abs_interval(pitch):
    return pitch.interval + (pitch.octave - 1) * 12

def parse_score(score_str, notes = False):
    print(f'score: {score_str}')
    if score_str == '': return []
    score = score_str.split(',')
    fn = parse_note if notes else parse_pitch
    return [fn(p) for p in score]

def extract_scale(score):
    scale = list(set([p.interval for p in score]))
    scale.sort()
    return scale


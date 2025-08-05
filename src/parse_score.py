from collections import namedtuple
from scale import scale_pitch, scale_step

class WrongScorePitch(Exception):
    def __init__(self, pitch): self.pitch = pitch
    def __str__ (self): return 'Wrong pitch symbol'

ScorePitch = namedtuple('Score_Pitch', ['step', 'octave', 'interval'])


def parse_note(score, parse_note=False):
    # score like a#/1, bb/2, D/3 .. 
    pitch_pair = score.strip().split('/') # octave delimiter
    try:
        step_part = pitch_pair[0]

        if parse_note:
            # score like a#/1, bb/2, D/3 .. 
            step = scale_step(step_part[0])
        else:
            # score like 1#/1, 3b/2, 4/3 .. 
            step = int(step_part[0])

        pitch  = scale_pitch(step)
            
        alter_char = step_part[1] if len(step_part) > 1 else None
        step_str = str(step) + (alter_char if alter_char else '')
        octave = int(pitch_pair[1]) if len(pitch_pair) > 1 else 1
        interval = pitch[1] + (octave - 1) * 12 if pitch else -2 #error
        interval_alt = interval+1 if alter_char == '#' else (interval-1 if alter_char == 'b' else interval)
    except Exception as e:
        print(e)
        raise WrongScorePitch(str)

    return ScorePitch(step_str, 1 if octave == 0 else octave, interval_alt)

def parse_score(score_str, score_notes=False):
    print(f'score: {score_str}')
    if score_str == '': return []
    score = score_str.split(',')
    return [parse_note(p, score_notes) for p in score]

def score_to_scale_intervals(score):
    '''
    score -> scale of chromatic intervals
    score : [ScorePitch]
    '''
    return scale_intervals(score_steps_to_scale([p.interval for p in score]))

def score_steps_to_scale(chrom_steps):
    scale = list(set(chrom_steps))
    scale.sort()
    min_interval = min(scale)
    return [p - min_interval for p in scale]

def scale_intervals(scale):
    return [scale[i] - scale[i-1] for i in range(1, len(scale))]

def get_score_scale_intervals(score, score_notes=False):
    '''
    score : string
    '''
    return score_to_scale_intervals(parse_score(score, score_notes))

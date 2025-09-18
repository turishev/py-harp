from typing import TypeAlias

from collections import namedtuple
from scale import scale_pitch, scale_step

ScorePitch = namedtuple('ScorePitch', ['step', 'octave', 'interval'])

ScoreType : TypeAlias = list[ScorePitch]

class WrongScorePitch(Exception):
    def __init__(self, pitch): self.pitch = pitch
    def __str__ (self): return 'Wrong pitch symbol'


def parse_note(note : str, use_letters=False) -> ScorePitch:
    '''
    note is letters: like a#/1, bb/2, D/3 .., when use_letters=True
    or
    note is scale step: like 1/1, 2b, 3#/2
    '''
    pitch_pair = note.strip().split('/') # octave delimiter
    try:
        step_part = pitch_pair[0]
        step = scale_step(step_part[0]) if use_letters else int(step_part[0])
        pitch = scale_pitch(step)
        alter_char = step_part[1] if len(step_part) > 1 else None
        step_str = str(step) + (alter_char if alter_char else '')
        octave = int(pitch_pair[1]) if len(pitch_pair) > 1 else 1
        interval = pitch[1] + (octave - 1) * 12 if pitch else -2 #error
        interval_alt = interval + 1 if alter_char == '#' else (interval - 1 if alter_char == 'b' else interval)
    except Exception as e:
        print(e)
        raise WrongScorePitch(str)

    return ScorePitch(step_str, 1 if octave == 0 else octave, interval_alt)


def parse_score(score_str : str, score_notes=False) -> list[ScorePitch]:
    if score_str == '': return []
    score = score_str.split(',')
    return [parse_note(p, score_notes) for p in score]


def _score_steps_to_scale(chrom_steps : list[int]) -> list[int]:
    '''
    returns sorted intervals, started from 0 (normalized) 
    '''
    scale = list(set(chrom_steps))
    scale.sort()
    min_interval = min(scale)
    return [p - min_interval for p in scale]


def get_score_scale(score : ScoreType) -> list[int]:
    return _score_steps_to_scale([p.interval for p in score])



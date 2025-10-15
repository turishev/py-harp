from dataclasses import dataclass
from typing import TypeAlias
from scale import scale_pitch, scale_step

@dataclass(frozen=True, slots=True)
class ScorePitch:
    step : str # string representations a major scale step, contains numbers and # and b
    octave : int # a scale octave
    interval : int # interval in half-steps, relative to the scale root, started from 0


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
        if step is None: raise WrongScorePitch(str)

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


def get_score_scale(score : list[ScorePitch]) -> list[int]:
    '''
    returns: list[int], sorted in ascending order, is not normalized
    '''
    intervals = [p.interval for p in score]
    scale = list(set(intervals))
    scale.sort()
    return scale


def normalize_scale(scale : list[int]) -> list[int]:
    if scale == []: return []
    elif scale[0] != 0: return [p - scale[0] for p in scale]
    else: return scale


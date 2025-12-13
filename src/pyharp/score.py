# from dataclasses import dataclass
# from typing import TypeAlias
from scale import scale_step_pitch, scale_step, note_pitch


class WrongScorePitch(Exception):
    def __init__(self, pitch): self.pitch = pitch
    def __str__ (self): return 'Wrong pitch symbol'


def split_note(note : str) -> tuple[str, int, int]:
    '''
    note like 1/1, 2b, 3#/2  or a/2 or bb/3
    '''
    pitch_pair = note.strip().split('/') # octave delimiter
    try:
        step_part = pitch_pair[0]
        alter_char = step_part[1] if len(step_part) > 1 else ''
        alt = 1 if alter_char == '#' else (-1 if alter_char == 'b' else 0)
        octave = int(pitch_pair[1]) if len(pitch_pair) > 1 else 1
        return (step_part[0], alt, octave)
    except Exception as e:
        print(e)
        raise WrongScorePitch(str)


def parse_step(step_str : str) -> int:
    '''
    note is scale step: like 1/1, 2b, 3#/2
    '''
    step_str,alt,octave =  split_note(step_str)

    try:
        step = int(step_str)
    except Exception as e:
        print(e)
        raise WrongScorePitch(step_str)

    pitch = scale_step_pitch(step)
    if pitch is not None:
        return  pitch + (octave - 1) * 12 + alt
    else:
        raise WrongScorePitch(step_str)


def parse_note(note : str) -> int:
    '''
    note like a#/1, bb/2, D/3
    root is letter
    '''
    step_part,alt,octave =  split_note(note)
    pitch = note_pitch(step_part)

    if pitch is not None:
        return pitch + (octave - 1) * 12 + alt
    else:
        raise WrongScorePitch(note)


def parse_steps(steps : str) -> list[int]:
    if steps == '': return []
    step_list = steps.split(',')
    return [parse_step(p) for p in step_list]


def parse_score(score_str : str, root : str) -> list[int]:
    if score_str == '': return []
    root_pitch = parse_note(root)
    score = score_str.split(',')
    score_shift = 0 if root_pitch == 0 else (root_pitch // 12 + 1) * 12 - root_pitch
    return [parse_note(p) + score_shift for p in score]


def get_score_scale(score : list[int]) -> list[int]:
    '''
    returns: list[int], sorted in ascending order, is not normalized
    '''
    scale = list(set(score))
    scale.sort()
    return scale


# def normalize_scale(scale : list[int]) -> list[int]:
#     if scale == []: return []
#     elif scale[0] != 0: return [p - scale[0] for p in scale]
#     else: return scale


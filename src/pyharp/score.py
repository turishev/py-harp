# from dataclasses import dataclass
# from typing import TypeAlias
from scale import get_scale_degree, get_scale_step, get_note_scale_degree


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
    step_str : str, scale step: like 1/1, 2b, 3#/2
    return : int, interval in the scale
    '''
    step_str,alt,octave =  split_note(step_str)

    try:
        step = int(step_str)
    except Exception as e:
        print(e)
        raise WrongScorePitch(step_str)

    pitch = get_scale_degree(step)

    if pitch is not None:
        return  pitch + (octave - 1) * 12 + alt
    else:
        raise WrongScorePitch(step_str)


def parse_note(note : str) -> int:
    '''
    note : str, note description like a#/1, bb/2, D/3
    return : int, the 'C' scale  degree
    '''
    step_part,alt,octave =  split_note(note)
    pitch = get_note_scale_degree(step_part)

    if pitch is not None:
        return pitch + (octave - 1) * 12 + alt
    else:
        raise WrongScorePitch(note)


def parse_steps(steps : str) -> list[int]:
    '''
    steps : str, comma-separated list of step signatures like 1#, 2b, 3/2
    return : list of intervals in the scale
    '''
    if steps == '': return []
    step_list = steps.split(',')
    return [parse_step(p) for p in step_list]


def parse_score(score_str : str, root : str) -> list[int]:
    '''
    score_str : str, comma-separated list of note signatures
    root : str, root note signature
    return : list of a scale degrees that specified of root note
    '''
    if score_str == '': return []
    root_scale_degree = parse_note(root)
    score = score_str.split(',')
    score_shift = 0 if root_scale_degree == 0 else (root_scale_degree // 12 + 1) * 12 - root_scale_degree
    return [parse_note(p) + score_shift for p in score]


def get_score_scale(score : list[int]) -> list[int]:
    '''
    score : list[int], list of scale degrees, unsorted, not unique 
    return : list[int], scale - list of unique scale degrees, sorted in ascending order
    '''
    scale = list(set(score))
    scale.sort()
    return scale


# def normalize_scale(scale : list[int]) -> list[int]:
#     if scale == []: return []
#     elif scale[0] != 0: return [p - scale[0] for p in scale]
#     else: return scale

from typing import Union, Optional
from math import ceil
C_MAJOR_SCALE = [('c', 0), ('d', 2), ('e', 4), ('f', 5), ('g', 7), ('a', 9), ('b', 11)]


def scale_step_pitch(step : int) -> Optional[int]:
    if step < 1 or step > 7: return None
    return C_MAJOR_SCALE[step - 1][1]

def scale_step(letter : str) -> Optional[int]:
    ll = letter.lower()
    for i,p in enumerate(C_MAJOR_SCALE):
        if p[0] == ll: return i + 1
    return None

def note_pitch(letter : str) -> Optional[int]:
    ll = letter.lower()
    for _,p in enumerate(C_MAJOR_SCALE):
        if p[0] == ll: return p[1]
    return None


def interval_to_step(interval : int) -> str:
    if interval < 0: return ''
    octave = interval // 12
    step_chrom = interval % 12
    if step_chrom == 0: step = '1'
    elif step_chrom <= 2: step = '2'
    elif step_chrom <= 4: step = '3'
    elif step_chrom <= 5: step = '4'
    elif step_chrom <= 7: step = '5'
    elif step_chrom <= 9: step = '6'
    elif step_chrom <= 11: step = '7'
    else: step = ''

    maj_steps = [p[1] for p in C_MAJOR_SCALE]
    alt = 'b' if not step_chrom in maj_steps else ''

    return step + alt + ('/' + str(octave + 1) if octave > 0 else '')


def interval_to_note(interval : int) -> str:
    if interval < 0: return ''
    octave = interval // 12
    step_chrom = interval % 12
    if step_chrom == 0: step = 'c'
    elif step_chrom <= 2: step = 'd'
    elif step_chrom <= 4: step = 'e'
    elif step_chrom <= 5: step = 'f'
    elif step_chrom <= 7: step = 'g'
    elif step_chrom <= 9: step = 'a'
    elif step_chrom <= 11: step = 'b'
    else: step = ''

    maj_steps = [p[1] for p in C_MAJOR_SCALE]
    alt = 'b' if not step_chrom in maj_steps else ''

    return step + alt + ('/' + str(octave + 1) if octave > 0 else '')

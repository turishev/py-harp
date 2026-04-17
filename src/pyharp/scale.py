from typing import Union, Optional
from math import ceil
C_MAJOR_SCALE = [('c', 0), ('d', 2), ('e', 4), ('f', 5), ('g', 7), ('a', 9), ('b', 11)]


def get_scale_degree(step : int) -> Optional[int]:
    if step < 1 or step > 7: return None
    return C_MAJOR_SCALE[step - 1][1]

def get_scale_step(letter : str) -> Optional[int]:
    ll = letter.lower()
    for i,p in enumerate(C_MAJOR_SCALE):
        if p[0] == ll: return i + 1
    return None

def get_note_scale_degree(letter : str) -> Optional[int]:
    ll = letter.lower()
    for _,p in enumerate(C_MAJOR_SCALE):
        if p[0] == ll: return p[1]
    return None


def scale_degree_to_step(interval : int) -> str:
    '''
    interval : chromatic interval in the major scale
    return : str, that represents step number with optional alteration sign # or b
    '''
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


def scale_degree_to_note(interval : int) -> str:
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

def create_inversions(scale : list[int]) -> list[list[int]]:
    '''
    scale : list[int], ordered scale degrees list
    return : list[list[int]], its items all are cyclic shifted original scale 
    '''
    result = [scale]
    for _ in range(0, len(scale) - 1):
        prev = result[-1]
        next = prev[1:]
        next.append(prev[0] + 12)
        oct_num = next[0] // 12
        next_norm = next if oct_num == 0 else [x - oct_num * 12 for x in next]
        result.append(next_norm)
    return result

from math import ceil
C_MAJOR_SCALE = [('c', 0), ('d', 2), ('e', 4), ('f', 5), ('g', 7), ('a', 9), ('b', 11)]


def scale_pitch(step : int) -> tuple[str, int] | None:
    if step < 1 or step > 7: return None
    return C_MAJOR_SCALE[step - 1]


def find_pitch(letter) -> tuple[str, int] | None:
    ll = letter.lower()
    for i,p in enumerate(C_MAJOR_SCALE):
        if p[0] == ll: return C_MAJOR_SCALE[i]
    return None


def note_pitch(note : str) -> int | None:
    '''
    returns: int if found or None
    note : str consists of step letter and (maybe) alteration sign
    like c# or db or Fb or G
    '''
    alter_char = note[1] if len(note) > 1 else ''
    alter_pitch = {'#': 1, 'b': -1, '':0 }.get(alter_char)
    if alter_pitch is None: return None
    pitch = find_pitch(note[0])
    if pitch is None: return None
    return pitch[1] + alter_pitch


def scale_step(letter : str) -> int | None:
    ll = letter.lower()
    for i,p in enumerate(C_MAJOR_SCALE):
        if p[0] == ll: return i + 1
    return None


def interval_to_step(interval : int) -> str:
    if interval < 0: return ''
    octave = ceil(interval // 12)
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

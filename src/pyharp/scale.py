
MAJOR_SCALE = [('c', 0), ('d', 2), ('e', 4), ('f', 5), ('g', 7), ('a', 9), ('b', 11)]


def scale_pitch(step):
    if step < 1 or step > 7: return None
    return MAJOR_SCALE[step - 1]
    
    
def find_pitch(letter):
    ll = letter.lower()
    for i,p in enumerate(MAJOR_SCALE):
        if p[0] == ll: return MAJOR_SCALE[i]
    return None

def note_pitch(note):
    alter_char = note[1] if len(note) > 1 else ''
    alter_pitch = {'#': 1, 'b': -1, '':0 }.get(alter_char)
    if alter_pitch is None: return None
    pitch = find_pitch(note[0])
    if pitch is None: return None
    return pitch[1] + alter_pitch


def scale_step(letter):
    ll = letter.lower()
    for i,p in enumerate(MAJOR_SCALE):
        if p[0] == ll: return i + 1
    return None

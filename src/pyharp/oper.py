from __future__ import annotations # for list annotations
from typing import Mapping, Optional

from output import ScaleLayout, format_pitch, format_layouts
from score  import parse_score, parse_steps, get_score_scale
from harmonicas import known_harmonicas_list
import harp_utils as hu #  HarpPitch, scale_to_layout, get_harp_scale, get_harp_key
import chords
import scale


def _format_scale_layout(position : int, scale_root : str, layout : list[tuple[int, list[hu.HarpPitch]]]) -> ScaleLayout:
    harp_key = hu.get_harp_key(position, scale_root)
    scale_formatted = [
        (
            scale.scale_degree_to_step(pair[0]), # scale step
            ','.join([format_pitch(p.hole, p.slide, p.method) for p in pair[1]]) # harp hole+method list
        )
        for pair in layout
    ]
    return ScaleLayout(harp_key, position, scale_root, scale_formatted)


def _get_formatted_layouts(score_scale : list[int],
                           scale_root : str,
                           harp_name : str,
                           drawbend=False, blowbend=False, overblow=False, overdraw=False,
                           exactly=False
                           ) -> list[ScaleLayout]:
    layouts : list[tuple[int, list[tuple[int, list[hu.HarpPitch]]]]] = hu.scale_to_layout(harp_name,
                                                                                          score_scale,
                                                                                          drawbend,
                                                                                          blowbend,
                                                                                          overblow,
                                                                                          overdraw,
                                                                                          exactly)
    formatted = [_format_scale_layout(layout[0], scale_root, layout[1]) for layout in layouts]
    return sorted(formatted, key=lambda v: v.position)


def find_harps_for_score(score : str, root : str, use_letters : bool,
                         harp_tuning : Optional[str],
                         harp_key : Optional[str],
                         drawbend : bool, blowbend : bool, overblow : bool, overdraw : bool,
                         exactly : bool
                         ) -> Mapping[str, list[ScaleLayout]]:
    '''
    find a suitable harp for a score,
    harps: comma-separated str, is used to limit output list by desirable harmonica types
    use_letters : boolean - use note letters instead interval numbers
    returns: dict which keys are harp-tuning names and values is list of lists of pair of a scale step
    and a harmonica hole-method
    '''
    layouts = {}
    harp_tunnings_list = known_harmonicas_list.keys() if harp_tuning is None else harp_tuning.lower().split(',')
    harp_keys_list = [] if harp_key is None else harp_key.lower().split(',')

    if use_letters:
        score_scale_degrees = parse_score(score, root)
    else:
        score_scale_degrees = parse_steps(score)

    score_scale =  get_score_scale(score_scale_degrees)
    # print(score_scale)

    for tuning in harp_tunnings_list:
        formatted_layouts = _get_formatted_layouts(score_scale, root, tuning,
                                                   drawbend, blowbend, overblow, overdraw,
                                                   exactly)
        if harp_keys_list != []:
            formatted_layouts = [l for l in formatted_layouts if l.harp_key in harp_keys_list]
        if formatted_layouts != []: layouts[tuning] = formatted_layouts
    # print(layouts)
    return layouts


def find_harp_for_score_print(score : str, root : str, use_letters : bool,
                              harp_tuning : Optional[str],
                              harp_key : Optional[str],
                              drawbend : bool, blowbend : bool, overblow : bool, overdraw : bool,
                              exactly : bool,
                              ) -> None:
    print(format_layouts(find_harps_for_score(score,
                                              root if root else 'c',
                                              use_letters,
                                              harp_tuning,
                                              harp_key, # None means all harps and all positions
                                              drawbend, blowbend, overblow, overdraw,
                                              exactly)))


    
def _find_harp_for_chord(chord : str,
                         harp_tuning : Optional[str],
                         harp_key : Optional[str],
                         drawbend : bool, blowbend : bool, overblow : bool, overdraw : bool
                         ) -> Mapping[str, list[ScaleLayout]]:
    root,bass,scale = chords.parse_chord(chord) #TODO - return bass also
    scale_str = ','.join(scale)
    return find_harps_for_score(scale_str, root, False,
                                harp_tuning, harp_key,
                                drawbend, blowbend, overblow, overdraw, False)


def find_harp_for_chord_print(chord : str,
                              harp_tuning : Optional[str],
                              harp_key : Optional[str],
                              drawbend : bool, blowbend : bool, overblow : bool, overdraw : bool
                              ) -> None:
    res = _find_harp_for_chord(chord, harp_tuning, harp_key,
                               drawbend, blowbend, overblow, overdraw)
    print(format_layouts(res))



def harmonica_scale_print(harp_tuning :  str,
                          drawbend : bool, blowbend : bool, overblow : bool, overdraw : bool
                          ) -> None:
    harp = known_harmonicas_list[harp_tuning]
    harp_layout = harp['scale']
    hscale = hu.get_harp_scale(harp_layout, drawbend, blowbend, overblow, overdraw)
    score_scale = hu.get_harp_scale_degrees(hscale)
    layouts = {harp_tuning : _get_formatted_layouts(score_scale, 'c',
                                                    harp_tuning,
                                                    drawbend, blowbend, overblow, overdraw)}
    print(format_layouts(layouts))


def harmonica_list_print():
    for harp_name, opts in known_harmonicas_list.items():
        print(f"{harp_name} : {opts['description']}")

def print_chords_list():
    print(chords.make_chords_info())

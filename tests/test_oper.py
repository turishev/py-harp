import pytest
from dataclasses import dataclass

from oper import split_by_field, _merge_layouts
from output import ScaleLayout

# [
#             ScaleLayout('c', 1, 'b', []),
#             ScaleLayout('f', 2, 'c', []),
#             ScaleLayout('g', 12, ),
#             ScaleLayout('c', 1, ),
#             ScaleLayout(),
#         ]

@dataclass()
class Data:
    a : int
    b: int


def test_split_by_field():
    lst = [
        Data(1, 11),
        Data(2, 21),
        Data(1, 12),
        Data(2, 22),
        Data(2, 23),
        Data(1, 13),
    ]

    assert split_by_field(lst, 'a') == {
        1 : [Data(1, 11), Data(1, 12), Data(1, 13)],
        2 : [Data(2, 21), Data(2, 22), Data(2, 23)],
    }

    assert split_by_field(lst, 'b') == {
        11 : [Data(1, 11)],
        12 : [Data(1, 12)],
        13 : [Data(1, 13)],
        21 : [Data(2, 21)],
        22 : [Data(2, 22)],
        23 : [Data(2, 23)],
    }

def test__merge_layouts(layouts):
    layouts = [
        {'richter': [
            ScaleLayout(harp_key='c', position=1, scale_root='c',
                        layout=[('1', '+1'), ('3', '+2'), ('5', '+3,-2')]),
            ScaleLayout(harp_key='c', position=1, scale_root='c',
                        layout=[('1', '+4'), ('3', '+5'), ('5', '+6')]),
            ScaleLayout(harp_key='c', position=1, scale_root='c',
                        layout=[('1', '+7'), ('3', '+8'), ('5', '+9')]),
            ScaleLayout(harp_key='f', position=2, scale_root='c',
                        layout=[('1', '+3,-2'), ('3', '-3'), ('5', '-4')]),
            ScaleLayout(harp_key='f', position=2, scale_root='c',
                        layout=[('1', '+6'), ('3', '-7'), ('5', '-8')]),
            ScaleLayout(harp_key='g', position=12, scale_root='c',
                        layout=[('1', '-5'), ('3', '-6'), ('5', '+7')]),
            ScaleLayout(harp_key='g', position=12, scale_root='c',
                        layout=[('1', '-9'), ('3', '-10'), ('5', '+10')])]},
        {'richter': [
            ScaleLayout(harp_key='c', position=1, scale_root='c',
                        layout=[('1', '+1'), ('3', '+2'), ('5', '+3,-2')]),
            ScaleLayout(harp_key='c', position=1, scale_root='c',
                        layout=[('1', '+4'), ('3', '+5'), ('5', '+6')]),
            ScaleLayout(harp_key='c', position=1, scale_root='c',
                        layout=[('1', '+7'), ('3', '+8'), ('5', '+9')]),
            ScaleLayout(harp_key='f', position=2, scale_root='c',
                        layout=[('1', '+3,-2'), ('3', '-3'), ('5', '-4')]),
            ScaleLayout(harp_key='f', position=2, scale_root='c',
                        layout=[('1', '+6'), ('3', '-7'), ('5', '-8')]),
            ScaleLayout(harp_key='g', position=12, scale_root='c',
                        layout=[('1', '-5'), ('3', '-6'), ('5', '+7')]),
            ScaleLayout(harp_key='g', position=12, scale_root='c',
                        layout=[('1', '-9'), ('3', '-10'), ('5', '+10')])]},
        {'richter': [
            ScaleLayout(harp_key='c', position=1, scale_root='c',
                        layout=[('1', '+1'), ('3', '+2'), ('5', '+3,-2')]),
            ScaleLayout(harp_key='c', position=1, scale_root='c',
                        layout=[('1', '+4'), ('3', '+5'), ('5', '+6')]),
            ScaleLayout(harp_key='c', position=1, scale_root='c',
                        layout=[('1', '+7'), ('3', '+8'), ('5', '+9')]),
            ScaleLayout(harp_key='f', position=2, scale_root='c',
                        layout=[('1', '+3,-2'), ('3', '-3'), ('5', '-4')]),
            ScaleLayout(harp_key='f', position=2, scale_root='c',
                        layout=[('1', '+6'), ('3', '-7'), ('5', '-8')]),
            ScaleLayout(harp_key='g', position=12, scale_root='c',
                        layout=[('1', '-5'), ('3', '-6'), ('5', '+7')]),
            ScaleLayout(harp_key='g', position=12, scale_root='c',
                        layout=[('1', '-9'), ('3', '-10'), ('5', '+10')])]}
    ]

    assert(_merge_layouts(layouts) == {
        'richter': [
            ScaleLayout(harp_key='c', position=1, scale_root='c', layout=[('1', '+1'), ('3', '+2'), ('5', '+3,-2')]),
            ScaleLayout(harp_key='c', position=1, scale_root='c', layout=[('1', '+4'), ('3', '+5'), ('5', '+6')]), 
            ScaleLayout(harp_key='c', position=1, scale_root='c', layout=[('1', '+7'), ('3', '+8'), ('5', '+9')]), 
            ScaleLayout(harp_key='f', position=2, scale_root='c', layout=[('1', '+3,-2'), ('3', '-3'), ('5', '-4')]), ScaleLayout(harp_key='f', position=2, scale_root='c', layout=[('1', '+6'), ('3', '-7'), ('5', '-8')]), ScaleLayout(harp_key='g', position=12, scale_root='c', layout=[('1', '-5'), ('3', '-6'), ('5', '+7')]), ScaleLayout(harp_key='g', position=12, scale_root='c', layout=[('1', '-9'), ('3', '-10'), ('5', '+10')])]
                                       })


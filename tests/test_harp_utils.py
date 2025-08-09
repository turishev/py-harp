import pytest
from harp_utils import get_harp_scale
from harmonicas import Method

def test_get_harp_scale():
    print(get_harp_scale("richter"))
    assert get_harp_scale("richter") == [
        (0, 1, Method.BLOW),
        (2, 1, Method.DRAW),
        (4, 2, Method.BLOW),
        (7, 2, Method.DRAW), 
        (7, 3, Method.BLOW),
        (11, 3, Method.DRAW), 
        (12, 4, Method.BLOW),
        (14, 4, Method.DRAW),
        (16, 5, Method.BLOW),
        (17, 5, Method.DRAW),
        (19, 6, Method.BLOW),
        (21, 6, Method.DRAW), 
        (23, 7, Method.DRAW), 
        (24, 7, Method.BLOW),
        (26, 8, Method.DRAW), 
        (28, 8, Method.BLOW), 
        (29, 9, Method.DRAW), 
        (31, 9, Method.BLOW), 
        (33, 10, Method.DRAW), 
        (36, 10, Method.BLOW)
    ]

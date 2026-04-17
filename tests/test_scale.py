import pytest

import scale

def test_create_inversions():
    assert scale.create_inversions([1,2,3,4]) == [
        [1,2,3,4],
        [2,3,4,13],
        [3,4,13,14],
        [4,13,14,15],
    ]

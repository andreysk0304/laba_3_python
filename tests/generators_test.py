import pytest

from src.exceptions import LowerBiggestHeighError
from src.test_keys.many_duplicates import many_duplicates
from src.test_keys.nearly_sorted import nearly_sorted
from src.test_keys.rand_float_array import rand_float_array
from src.test_keys.rand_int_array import rand_int_array


def test_seeds():
    assert many_duplicates(100, seed=993) == many_duplicates(100, seed=993)
    assert nearly_sorted(100, 5, seed=993) == nearly_sorted(100, 5, seed=993)
    assert rand_int_array(100, 1, 10, seed=993) == rand_int_array(100, 1, 10, seed=993)
    assert rand_float_array(100, seed=993) == rand_float_array(100, seed=993)


def test_lo_biggest_hi_error():
    with pytest.raises(LowerBiggestHeighError):
        rand_int_array(10, 10, 1)
    with pytest.raises(LowerBiggestHeighError):
        rand_float_array(10, 10, 1)


def test_rand_int_array_distinct_range_too_small():
    with pytest.raises(ValueError):
        rand_int_array(10, 0, 5, distinct=True)


def test_distinct_random_int():
    a = rand_int_array(10, 10, 100, distinct=True)
    assert len(a) == len(set(a))
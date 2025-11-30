import random
import pytest

from src.test_keys.many_duplicates import many_duplicates
from src.test_keys.nearly_sorted import nearly_sorted
from src.test_keys.rand_float_array import rand_float_array
from src.test_keys.rand_int_array import rand_int_array
from src.test_keys.reverse_sorted import reverse_sorted

from src.functions.sorts.bubble_sort import bubble_sort
from src.functions.sorts.bucket_sort import bucket_sort
from src.functions.sorts.counting_sort import counting_sort
from src.functions.sorts.heap_sort import heap_sort
from src.functions.sorts.quick_sort import quick_sort
from src.functions.sorts.radix_sort import radix_sort


INT_SORTS = [
    bubble_sort,
    heap_sort,
    quick_sort,
]

NON_NEGATIVE_SORTS = [
    radix_sort,
    counting_sort,
]

BUCKET_SORTS = [
    bucket_sort,
]


@pytest.mark.repeat(10)
@pytest.mark.parametrize("sort", INT_SORTS)
def test_int_sorts_on_full_range(sort):
    test_list = rand_int_array(100, -100, 100)
    assert sort(test_list) == sorted(test_list)

    test_list = many_duplicates(100)
    assert sort(test_list) == sorted(test_list)

    test_list = nearly_sorted(100, random.randint(0, 100))
    assert sort(test_list) == sorted(test_list)

    test_list = reverse_sorted(100)
    assert sort(test_list) == sorted(test_list)


@pytest.mark.repeat(10)
@pytest.mark.parametrize("sort", NON_NEGATIVE_SORTS)
def test_non_negative_sorts(sort):
    test_list = rand_int_array(100, 0, 200)
    assert sort(test_list) == sorted(test_list)


@pytest.mark.repeat(10)
@pytest.mark.parametrize("sort", BUCKET_SORTS)
def test_bucket_sort(sort):
    test_list = rand_float_array(100, 0, 1)
    assert sort(test_list) == sorted(test_list)

from src.benchmarks.timeit_once import timeit_once
from src.functions.sorts.quick_sort import quick_sort
from src.functions.sorts.radix_sort import radix_sort
from src.test_keys.rand_float_array import rand_float_array

from src.test_keys.rand_int_array import rand_int_array

from src.functions.sorts.bubble_sort import bubble_sort
from src.functions.sorts.bucket_sort import bucket_sort
from src.functions.sorts.counting_sort import counting_sort
from src.functions.sorts.heap_sort import heap_sort

N = [10, 100, 1000, 10000, 100000]

BIG_N = [100, 1000, 10000, 100000, 1000000, 10000000]

def get_bubble_sort_time() -> None:
    print('Bubble sort')
    for n in N:
        test_list = rand_int_array(n, 1, 1000000)

        print(f'{n} -> {timeit_once(bubble_sort, test_list)} sec')

    return


def get_bucket_sort_time() -> None:
    print('Bucket sort')
    for n in BIG_N:
        test_list = rand_float_array(n, 0, 1)

        print(f'{n} -> {timeit_once(bucket_sort, test_list)} sec')

    return


def get_counting_sort() -> None:
    print('Counting sort')
    for n in BIG_N:
        test_list = rand_int_array(n, 1, 100000000)

        print(f'{n} -> {timeit_once(counting_sort, test_list)} sec')

    return


def get_heap_sort() -> None:
    print('Heap sort')
    for n in BIG_N:
        test_list = rand_int_array(n, 1, 100000000)

        print(f'{n} -> {timeit_once(heap_sort, test_list)} sec')

    return


def get_quick_sort() -> None:
    print('Quick sort')
    for n in BIG_N:
        test_list = rand_int_array(n, 1, 100000000)

        print(f'{n} -> {timeit_once(quick_sort, test_list)} sec')

    return


def get_radix_sort() -> None:
    print('Radix sort')
    for n in BIG_N:
        test_list = rand_int_array(n, 1, 100000000)

        print(f'{n} -> {timeit_once(radix_sort, test_list)} sec')

    return


if __name__ == '__main__':
    get_radix_sort()
    get_quick_sort()
    get_heap_sort()
    get_counting_sort()
    get_bucket_sort_time()
    get_bubble_sort_time()
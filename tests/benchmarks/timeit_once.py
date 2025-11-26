from os import times_result
from time import perf_counter

def timeit_once(func, *args, **kwargs) -> float:

    time_start: float = perf_counter()
    func(*args, **kwargs)
    time_end: float = perf_counter()

    return time_end - time_start


def timeit_once_cli(func, *args, **kwargs):

    time_start: float = perf_counter()
    answer = func(*args, **kwargs)
    time_end: float = perf_counter()

    return time_end - time_start, answer
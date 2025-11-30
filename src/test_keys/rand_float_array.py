import random

from src.exceptions import LowerBiggestHeighError


def rand_float_array(n: int, lo: float | int = 0.0, hi: float | int = 1.0, *, seed = None) -> list[float]:
    if lo >= hi:
        raise LowerBiggestHeighError()

    if seed is not None:
        random.seed(seed)

    return [random.uniform(lo, hi) for _ in range(n)]
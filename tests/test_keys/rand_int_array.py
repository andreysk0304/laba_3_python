import random


def rand_int_array(n: int, lo: int, hi: int, *, distinct: bool = False, seed=None):

    if seed is not None:
        random.seed(seed)

    if distinct:
        if hi - lo + 1 < n:
            raise ValueError("Диапазон слишком мал для уникальных значений.")
        return random.sample(range(lo, hi + 1), n)

    return [random.randint(lo, hi) for _ in range(n)]
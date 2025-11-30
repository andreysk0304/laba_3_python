import pytest

from time import sleep

from src.benchmarks.timeit_once import timeit_once


def test_timeit_once():
    epsl = 0.1

    def one_second() -> None:
        sleep(1)

    assert 1 - epsl < timeit_once(one_second) < 1 + epsl

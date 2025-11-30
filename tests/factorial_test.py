import pytest
from src.functions.factorial import factorial_recursive, factorial
from src.exceptions import FactorialError


@pytest.mark.parametrize("value, answer", [(0, 1), (1, 1), (2, 2), (3, 6), (4, 24), (5, 120), (10, 3628800)])
def test_factorial(value, answer):
    assert factorial(value) == answer
    assert factorial_recursive(value) == answer


def test_factorial_errors():
    with pytest.raises(FactorialError):
        factorial_recursive(-1)
    with pytest.raises(FactorialError):
        factorial(-1)
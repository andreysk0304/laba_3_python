from src.exceptions import FibonacciError

def fibonacci(x: int) -> int:
    """

    :param x:
    :return:
    """

    if x < 0:
        raise FibonacciError('Последовательность определенна на числах больше нуля.')

    if x == 0:
        return 0

    if x == 1:
        return 1

    x1, x2 = 0, 1
    for _ in range(2, x+1):
        x1, x2 = x2, x1+x2

    return x2


def fibonacci_recursive(x: int) -> int:
    """

    :param x:
    :return:
    """

    if x < 0:
        raise FibonacciError('Последовательность определенна на числах больше нуля.')

    if x == 0:
        return 0

    if x == 1:
        return 1

    return fibonacci_recursive(x-1) + fibonacci_recursive(x-2)
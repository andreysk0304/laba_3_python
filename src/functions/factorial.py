from src.exceptions import FactorialError


def factorial(x: int) -> int:
    """
    Функция вычисляет факториал заданного числа.

    :param x: Число для которого вычисляется факториал.
    :return: Факториал числа.
    """

    if x < 0:
        raise FactorialError('Факториал определён только для положительных чисел.')
    if x == 0 or x == 1:
        return 1

    fact: int = 1
    while x>0:
        fact *= x
        x -= 1

    return fact


def factorial_recursive(x: int) -> int:
    """
    Функция вычисляет факториал рекурсивно.

    :param x: Число для которого вычисляется факториал.
    :return: Факториал числа
    """

    if x < 0:
        raise FactorialError('Факториал определён только для положительных чисел.')
    if x == 0 or x == 1:
        return 1

    return x * factorial_recursive(x-1)


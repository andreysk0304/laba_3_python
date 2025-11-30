def bubble_sort(x: list[int]) -> list[int]:
    """
    Функция bubble сортировки.

    Проходим по списку и сравниваем рядом стоящие пары чисел, если число слева больше числа справа, меняем их местами
    Уменьшаем область прохода списка (правые числа уже нет смысла проходить, они уже отсортированы).

    :param x: Входной не отсортированный список.
    :return: Отсортированный список по возрастанию.
    """

    count = len(x)
    if count <= 1:
        return x

    x = x.copy()

    for i in range(count - 1):
        swapped = False

        for j in range(count - i - 1):
            if x[j] > x[j + 1]:
                x[j], x[j + 1] = x[j + 1], x[j]
                swapped = True

        if not swapped:
            break

    return x
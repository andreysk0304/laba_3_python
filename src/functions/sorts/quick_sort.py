def quick_sort(x: list[int]) -> list[int]:
    """
    Функция quick сортировки.

    Берём опорный элемент (середину списка в этом случае, а можно брать случайное число или начало списка, это не важно)
    Делим список на два списка, первый с числами больше опорного элемента, второй с числами меньше опорного элемента
    Сортируем рекурсивно эти два списка, затем склеиваем их и возвращаем (Этой же фукнцией).

    :param a: Входной не отсортированный список.
    :return: Отсортированный список по возрастанию.ро
    """

    if len(x) <= 1:
        return x

    pivot = x[len(x) // 2]
    less_pivot = [a for a in x if a < pivot]
    middle = [a for a in x if a == pivot]
    more_pivot = [a for a in x if a > pivot]

    return quick_sort(less_pivot) + middle + quick_sort(more_pivot)



def quick_sort_for_float(x: list[float]) -> list[float]:
    """
        Функция quick сортировки для float.

        Берём опорный элемент (середину списка в этом случае, а можно брать случайное число или начало списка, это не важно)
        Делим список на два списка, первый с числами больше опорного элемента, второй с числами меньше опорного элемента
        Сортируем рекурсивно эти два списка, затем склеиваем их и возвращаем (Этой же фукнцией).

        :param a: Входной не отсортированный список.
        :return: Отсортированный список по возрастанию.ро
    """

    if len(x) <= 1:
        return x

    pivot = x[len(x) // 2]
    less_pivot = [a for a in x if a < pivot]
    middle = [a for a in x if a == pivot]
    more_pivot = [a for a in x if a > pivot]

    return quick_sort_for_float(less_pivot) + middle + quick_sort_for_float(more_pivot)
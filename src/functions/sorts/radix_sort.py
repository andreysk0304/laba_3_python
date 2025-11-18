def radix_sort(x: list[int], base: int = 10) -> list[int]:
    """
    Функция поразрядной (radix) сортировки.

    Сортирует целые числа, проходя по каждому разряду (единицы, десятки, сотни и т.д.).
    На каждом шаге выполняется стабильная сортировка (в нашем случае counting sort) по текущему разряду.
    Начинаем с младших разрядов и двигаемся к старшим, пока не будут обработаны все цифры самого большого числа.

    :param x: Входной неотсортированный список.
    :param base: Основание системы счисления (по умолчанию 10 — десятичная).
    :return: Новый список, отсортированный по возрастанию.
    """

    if not x:
        return []

    max_value = max(x)
    exp = 1

    while max_value // exp > 0:
        count = [0] * base
        output = [0] * len(x)

        for num in x:
            index = (num // exp) % base
            count[index] += 1

        for i in range(1, base):
            count[i] += count[i - 1]

        for num in reversed(x):
            index = (num // exp) % base
            output[count[index] - 1] = num
            count[index] -= 1

        x = output[:]
        exp *= base

    return x

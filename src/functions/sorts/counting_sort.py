def counting_sort(x: list[int]) -> list[int]:
    """
    Функция counting сортировки.

    Выделяем максимальный и минимальный элемент списка (max_value, min_value), находим промежуток в которых находятся все числа списка
    Проходим по полученному промежутку и считаем сколько таких элементов встречается в списке
    Проходим по количествам и собираем новый список, добавляя элементы по порядку и в нужном кол-ве.

    :param x: Входной не отсортированный список.
    :return: Отсортированный список.
    """

    min_value = min(x)
    max_value = max(x)

    count_values = max_value - min_value + 1

    values_counts = [0] * count_values

    for num in x:
        values_counts[num - min_value] += 1

    sorted_x = []
    for i, c in enumerate(values_counts):
        sorted_x.extend([i + min_value] * c)

    return sorted_x
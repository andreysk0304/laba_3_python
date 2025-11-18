def heapify(a: list[int], n: int, i: int) -> None:
    """
    Просеивание вниз — делает поддерево с корнем в i корректной max-кучей.

    :param a: массив
    :param n: размер кучи (части массива)
    :param i: индекс текущего узла
    """
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and a[left] > a[largest]:
        largest = left

    if right < n and a[right] > a[largest]:
        largest = right

    if largest != i:
        a[i], a[largest] = a[largest], a[i]
        heapify(a, n, largest)


def heap_sort(a: list[int]) -> list[int]:
    """
    Пирамидальная сортировка (Heap Sort).
    Сортирует список по возрастанию с использованием max-heap.

    :param a: Список целых чисел
    :return: Отсортированный список
    """

    n = len(a)
    a = a[:]

    for i in range(n // 2 - 1, -1, -1):
        heapify(a, n, i)

    for i in range(n - 1, 0, -1):
        a[0], a[i] = a[i], a[0]
        heapify(a, i, 0)

    return a

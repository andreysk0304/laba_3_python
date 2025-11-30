from src.functions.sorts.quick_sort import quick_sort_for_float


def bucket_sort(a: list[float], buckets: int | None = None) -> list[float]:
    """
    Функция bucket (корзинной) сортировки.

    Делит диапазон входных чисел на равные поддиапазоны (корзины),
    распределяет элементы по соответствующим корзинам, сортирует каждую корзину отдельно
    и затем объединяет результаты в один отсортированный список.

    :param a: Входной список чисел с плавающей точкой.
    :param buckets: Количество корзин (если None — выбирается автоматически).
    :return: Новый список, отсортированный по возрастанию.
    """
    if not a:
        return []

    if buckets is None:
        buckets = len(a)

    bucket_list = [[] for _ in range(buckets)]

    for num in a:
        if not 0 <= num < 1:
            raise ValueError("Элементы должны быть в диапазоне [0, 1]")
        index = int(num * buckets)
        bucket_list[index].append(num)

    for i in range(buckets):
        bucket_list[i] = quick_sort_for_float(bucket_list[i])

    sorted_a = [num for bucket in bucket_list for num in bucket]

    return sorted_a

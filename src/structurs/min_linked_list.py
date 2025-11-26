from src.structurs.min_node import MinNode


class MinLinkedList:
    node_class = MinNode

    def __init__(self):
        """
        Инициализирует пустой список с минимумами.
        """
        self.head = None
        self.size = 0

    def push_front(self, x: int) -> None:
        """
        Добавляет элемент в начало списка и вычисляет текущий минимум.

        :param x: Вставляемый элемент в список.
        :return: Ничего.
        """

        if self.head is None:
            new_min = x
        else:
            new_min = min(x, self.head.min_value)

        new_node = self.node_class(x, self.head, new_min)
        self.head = new_node
        self.size += 1

    def pop_front(self) -> int:
        """
        Функция удаляет значение из начала связанного списка.

        :return: Удалённое значение.
        """

        if self.head is None:
            raise IndexError("Связанный список пуст.")

        value = self.head.value
        self.head = self.head.next
        self.size -= 1
        return value

    def min(self) -> int:
        """
        Возвращает текущий минимум за O(1).

        :return: Минимальное значение списка.
        """

        if self.head is None:
            raise IndexError("Связанный список пуст.")

        return self.head.min_value

    def is_empty(self) -> bool:
        """
        Проверяет, пуст ли список.

        :return: True - пуст, False - не пуст.
        """
        return self.head is None

    def __len__(self) -> int:
        """
        Возвращает количество элементов в списке.

        :return: Длина списка.
        """
        return self.size

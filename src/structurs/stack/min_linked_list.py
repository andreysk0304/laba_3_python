from src.structurs.linked_list import LinkedList
from src.structurs.stack.min_node import MinNode


class MinLinkedList(LinkedList):
    node_class = MinNode

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

    def min(self) -> int:
        """
        Возвращает текущий минимум за O(1).

        :return: Минимальное значение списка.
        """

        if self.head is None:
            raise IndexError("Связанный список пуст.")

        return self.head.min_value
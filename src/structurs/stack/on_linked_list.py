from src.exceptions import StackIsEmpty
from src.structurs.stack.min_linked_list import MinLinkedList


class LinkedListStack:
    def __init__(self):
        self.list = MinLinkedList()


    def push(self, x: int) -> None:
        """
        Добавляет элемент на вершину стека.

        :param x: Элемент, добавляемый на вершину стэка.
        :return: Ничего
        """

        self.list.push_front(x)


    def pop(self) -> int:
        """
        Удаляет элемент с вершины стека и возвращает его.

        :return: Удалённый элемент с вершины стека.
        """

        return self.list.pop_front()


    def peek(self) -> int:
        """
        Показывает верхний элемент, не удаляя его.

        :return: Верхний элемент стека
        """

        if self.list.is_empty():
            raise StackIsEmpty()

        return self.list.head.value


    def min(self) -> int:
        """
        Возвращает минимальный элемент в стеке за O(1).

        :return: Минимальный элемент стэка.
        """
        return self.list.min()


    def is_empty(self) -> bool:
        """
        Функция проверяет, пуст ли стек.

        :return: True - стэк пуст, False - стэк не пуст.
        """
        return self.list.is_empty()


    def __len__(self) -> int:
        return len(self.list)
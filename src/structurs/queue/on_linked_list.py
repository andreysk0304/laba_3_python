from src.exceptions import QueueIsEmpty
from src.structurs.linked_list import LinkedList


class LinkedListQueue:
    def __init__(self):
        self.list = LinkedList()


    def enqueue(self, x: int) -> bool:
        """
        Добавляет элемент в конец очереди.

        :param x: Добавляемый элемент.
        :return: Ничего.
        """

        self.list.push_back(x)
        return True


    def dequeue(self) -> int:
        """
        Удаляет и возвращает элемент из начала очереди.

        :return: Элемент из начала очереди.
        """

        if self.is_empty():
            raise QueueIsEmpty()

        return self.list.pop_front()


    def front(self) -> int:
        """
        Возвращает первый элемент очереди, не удаляя его.

        :return: Элемент конца (первый по очерёдности) очереди.
        """

        if self.list.is_empty():
            raise QueueIsEmpty()

        return self.list.head.value


    def is_empty(self) -> bool:
        """
        Проверяет, пуста ли очередь.

        :return: True - очередь пуста, False - очередь не пуста.
        """

        return self.list.is_empty()


    def __len__(self) -> int:
        """
        Возвращает количество элементов в очереди.

        :return: Длинна очереди
        """

        return len(self.list)
from src.exceptions import QueueIsEmpty


class ListQueue:
    def __init__(self):
        self.data = []
        self.head = 0
        self.size = 0


    def enqueue(self, x: int) -> bool:
        """
        Добавляет элемент в конец очереди.

        :return: Добавляет элемент в конец очереди.
        """

        self.data.append(x)
        self.size += 1

        return True


    def dequeue(self) -> int:
        """
        Удаляет и возвращает элемент из начала очереди.

        :return: Удалённый элемент.
        """

        if self.is_empty():
            raise QueueIsEmpty()

        self.size -= 1
        self.head += 1

        return self.data[self.head-1]


    def front(self) -> int:
        """
        Возвращает первый элемент очереди.

        :return: Первый элемент очереди.
        """

        if not self.data:
            raise QueueIsEmpty()

        return self.data[0]


    def is_empty(self) -> bool:
        """
        Проверка на пустоту очереди.

        :return: True - очередь пуста, False - очередь не пуста.
        """

        return self.size == 0


    def __len__(self) -> int:
        """
        Количество элементов в очереди.

        :return: Длинна очереди
        """

        return self.size
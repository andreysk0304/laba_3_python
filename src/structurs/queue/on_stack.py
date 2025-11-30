from src.exceptions import QueueIsEmpty
from src.structurs.stack.on_linked_list import LinkedListStack


class QueueOnLinkedListStacks:
    def __init__(self):
        self.in_stack = LinkedListStack()
        self.out_stack = LinkedListStack()


    def enqueue(self, x: int) -> bool:
        """
        Добавляет элемент в очередь.

        :param x: Новый элемент очереди.
        :return: Ничего.
        """

        self.in_stack.push(x)
        return True


    def dequeue(self) -> int:
        """
        Удаляет и возвращает первый элемент очереди.

        :return: Первый элемент очереди.
        """

        if self.out_stack.is_empty():
            if self.in_stack.is_empty():
                raise QueueIsEmpty()

            while not self.in_stack.is_empty():
                self.out_stack.push(self.in_stack.pop())

        return self.out_stack.pop()


    def front(self) -> int :
        """
        Возвращает первый элемент очереди без удаления.

        :return: Первый элемент очереди.
        """

        if self.out_stack.is_empty():
            if self.in_stack.is_empty():
                raise QueueIsEmpty()

            while not self.in_stack.is_empty():
                self.out_stack.push(self.in_stack.pop())

        return self.out_stack.peek()


    def is_empty(self) -> bool:
        """
        Проверка на пустоту.

        :return: True - очередь пуста, False - очередь не пуста.
        """

        return self.in_stack.is_empty() and self.out_stack.is_empty()


    def __len__(self):
        """
        Возвращает размер очереди.

        :return: Длинна очереди.
        """

        return len(self.in_stack) + len(self.out_stack)
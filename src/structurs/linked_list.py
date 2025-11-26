from src.structurs.node import Node

class LinkedList:
    node_class = Node

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0


    def push_front(self, x: int) -> None:
        """
        Функция добавляет значение в начало связанного списка.

        :param x: Значение которое нужно добавить в список.
        :return: Ничего.
        """

        new_element = self.node_class(x, self.head)

        self.head = new_element

        if self.tail is None:
            self.tail = new_element

        self.size += 1


    def push_back(self, x: int) -> None:
        """
        Функция добавляет значение в конец связанного списка.

        :param x: Добавляемый элемент.
        :return: Ничего.
        """

        new_element = self.node_class(x)

        if self.tail is None:
            self.head = self.tail = new_element
        else:
            self.tail.next = new_element
            self.tail = new_element

        self.size += 1


    def pop_front(self) -> int:
        """
        Функция удаляет значение из начала связанного списка.

        :return: Удалённое значение
        """

        if self.head is None:
            raise IndexError("Связанный список пуст.")

        value = self.head.value
        self.head = self.head.next

        if self.head is None:
            self.tail = None

        self.size -= 1

        return value


    def is_empty(self) -> bool:
        """
        Функция проверки пустой ли связанный список пустым.

        :return: True - список пуст, False - список хранит значения.
        """

        return self.head is None


    def __len__(self):
        """
        Функция показывает текущую длинну связанного списка.

        :return: Длинна связанного списка.
        """

        return self.size
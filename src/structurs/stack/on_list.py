from src.exceptions import StackIsEmpty


class StackList:
    def __init__(self):
        self.data = []
        self.mins = []
        self.size = 0


    def push(self, x: int) -> bool:
        """
        Добавляет элемент на вершину стека.

        :param x: Элемент, который нужно добавить на вершину стэка.
        :return: Ничего.
        """

        self.data.append(x)

        if not self.mins or x <= self.mins[-1]:
            self.mins.append(x)

        self.size += 1

        return True


    def pop(self) -> int:
        """
        Удаляет и возвращает верхний элемент стека.

        :return: Возвращает удалённый элемент стэка.
        """

        if self.is_empty():
            raise StackIsEmpty()

        val = self.data.pop()

        if val == self.mins[-1]:
            self.mins.pop()

        self.size -= 1

        return val


    def peek(self) -> int:
        """
        Возвращает верхний элемент, не удаляя его.

        :return: Верхний элемент стэка.
        """

        if self.is_empty():
            raise StackIsEmpty()

        return self.data[-1]


    def min(self) -> int:
        """
        Возвращает минимальный элемент за O(1).

        :return: Минимальное значение стэка.
        """

        if self.is_empty():
            raise StackIsEmpty()

        return self.mins[-1]


    def is_empty(self) -> bool:
        """
        Функция проверяет, является ли стэк пустым.

        :return True - стэк пуст, False - стэк не имеет какие-то значения.
        """

        return self.size == 0


    def __len__(self) -> int:
        """
        Возвращает длинну стэка.

        :return: Длинна стэка.
        """
        return self.size
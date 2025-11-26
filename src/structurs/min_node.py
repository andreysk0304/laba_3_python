class MinNode:
    def __init__(self, value: int, next=None, min_value=None):
        """
        Узел для MinLinkedList

        :param value: Значение узла
        :param next: Следующий узел
        :param min_value: Минимум в стеке на момент добавления
        """

        self.value = value
        self.next = next
        self.min_value = min_value
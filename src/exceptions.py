class FactorialError(Exception):
    def __init__(self, msg: str):
        super().__init__(msg)


class FibonacciError(Exception):
    def __init__(self, msg: str):
        super().__init__(msg)


class StackIsEmpty(Exception):
    def __init__(self):
        super().__init__('Стэк пуст.')


class QueueIsEmpty(Exception):
    def __init__(self):
        super().__init__('Очередь пуста.')
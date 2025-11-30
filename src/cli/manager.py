from src.structurs.queue.on_linked_list import LinkedListQueue
from src.structurs.stack.on_linked_list import LinkedListStack
from src.test_keys.rand_float_array import rand_float_array
from src.test_keys.rand_int_array import rand_int_array


class CliManager:

    def __init__(self):
        self.test_int_list: list[int] = []
        self.test_float_list: list[float] = []

        self.stack = LinkedListStack()
        self.queue = LinkedListQueue()

        self.generate_int_test_list()
        self.generate_float_test_list()


    def generate_int_test_list(self, n: int = 10, lo: int = 1, hi: int = 100) -> None:
        self.test_int_list = rand_int_array(n, lo, hi)


    def generate_float_test_list(self, n: int = 10, lo: int = 0, hi: int = 1) -> None:
        self.test_float_list = rand_float_array(n, lo, hi)


    def clear_stack(self) -> None:
        self.stack = LinkedListStack()


    def clear_queue(self) -> None:
        self.queue = LinkedListQueue()
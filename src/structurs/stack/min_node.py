from src.structurs.node import Node

class MinNode(Node):
    def __init__(self, min_value: int, value: int, next=None):
        super().__init__(value, next)
        self.min_value = min_value
import pytest

from src.exceptions import StackIsEmpty
from src.structurs.stack.on_linked_list import LinkedListStack
from src.structurs.stack.on_list import StackList


def test_stack_on_linked_list():
    stack = LinkedListStack()

    assert stack.push(1)
    assert stack.push(2)
    assert stack.push(30)

    assert stack.min() == 1

    assert stack.is_empty() == False

    assert stack.peek() == 30

    assert stack.pop() == 30
    assert stack.pop() == 2
    assert stack.pop() == 1

    assert stack.is_empty() == True
    assert len(stack) == 0



def test_stack_list_pop_empty():
    s = StackList()
    with pytest.raises(StackIsEmpty):
        s.pop()

    s = LinkedListStack()
    with pytest.raises(StackIsEmpty):
        s.pop()



def test_stack_list_peek_empty():
    s = StackList()
    with pytest.raises(StackIsEmpty):
        s.peek()

    s = LinkedListStack()
    with pytest.raises(StackIsEmpty):
        s.peek()


def test_stack_list_min_empty():
    s = StackList()
    with pytest.raises(StackIsEmpty):
        s.min()

    s = LinkedListStack()
    with pytest.raises(StackIsEmpty):
        s.min()


def test_stack_on_list():
    stack = StackList()

    assert stack.push(1)
    assert stack.push(2)
    assert stack.push(30)

    assert stack.min() == 1

    assert stack.is_empty() == False

    assert stack.peek() == 30

    assert stack.pop() == 30
    assert stack.pop() == 2
    assert stack.pop() == 1

    assert stack.is_empty() == True
    assert len(stack) == 0
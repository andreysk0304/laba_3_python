import pytest

from src.exceptions import QueueIsEmpty
from src.structurs.queue.on_linked_list import LinkedListQueue
from src.structurs.queue.on_list import ListQueue
from src.structurs.queue.on_stack import QueueOnLinkedListStacks


def test_queue_on_linked_list():
    queue = LinkedListQueue()

    assert queue.enqueue(1)
    assert queue.enqueue(2)

    assert queue.dequeue() == 1
    assert queue.dequeue() == 2

    assert queue.is_empty() == True

    queue.enqueue(1)

    assert queue.front() == 1
    assert len(queue) == 1


def test_is_empty_front():
    q = ListQueue()
    with pytest.raises(QueueIsEmpty):
        q.front()

    q = LinkedListQueue()
    with pytest.raises(QueueIsEmpty):
        q.front()

    q = QueueOnLinkedListStacks()
    with pytest.raises(QueueIsEmpty):
        q.front()


def test_is_empty_dequeue():
    q = ListQueue()
    with pytest.raises(QueueIsEmpty):
        q.dequeue()

    q = LinkedListQueue()
    with pytest.raises(QueueIsEmpty):
        q.dequeue()

    q = QueueOnLinkedListStacks()
    with pytest.raises(QueueIsEmpty):
        q.dequeue()



def test_queue_on_list():
    queue = ListQueue()

    assert queue.enqueue(1)
    assert queue.enqueue(2)

    assert queue.dequeue() == 1
    assert queue.dequeue() == 2

    assert queue.is_empty() == True

    queue.enqueue(1)

    assert queue.front() == 1
    assert len(queue) == 1


def test_queue_on_stack():
    queue = QueueOnLinkedListStacks()

    assert queue.enqueue(1)
    assert queue.enqueue(2)

    assert queue.dequeue() == 1
    assert queue.dequeue() == 2

    assert queue.is_empty() == True

    queue.enqueue(1)

    assert queue.front() == 1
    assert len(queue) == 1
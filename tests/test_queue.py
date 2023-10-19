import pytest
from src.queue import Node, Queue


@pytest.fixture
def test_queue():
    return Queue()


def test_Node():
    """Функция для тестирования класса Node"""
    test_node1 = Node(1, None)
    test_node2 = Node(2, None)
    test_node1.next_node = test_node2

    assert test_node1.data == 1
    assert test_node1.next_node == test_node2
    assert test_node2.data == 2
    assert test_node2.next_node is None


def test_Queue_enqueue(test_queue):
    """Функция для тестирования метода enqueue класса Queue"""
    test_queue.enqueue(1)
    test_queue.enqueue(2)
    test_queue.enqueue(3)
    test_queue.enqueue(4)

    assert str(test_queue) == "1\n2\n3\n4"

    assert test_queue.head.data == 1
    assert test_queue.tail.data == 4
    assert test_queue.tail.next_node is None
    assert test_queue.head.next_node.next_node.data == 3


def test_Queue_dequeue(test_queue):
    """Функция для тестирования метода dequeue класса Queue"""
    test_queue.enqueue("data1")
    test_queue.enqueue("data2")
    test_queue.enqueue("data3")

    assert test_queue.dequeue() == "data1"
    assert test_queue.dequeue() == "data2"
    assert test_queue.dequeue() == "data3"
    assert test_queue.dequeue() is None

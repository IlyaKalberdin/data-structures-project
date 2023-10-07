import pytest

from src.stack import Node, Stack


def test_Node():
    """Функция для тестирования класса Node"""
    test_node1 = Node(10, None)
    test_node2 = Node(20, test_node1)

    assert test_node1.data == 10
    assert test_node1.next_node == None
    assert test_node2.data == 20
    assert test_node2.next_node == test_node1


def test_Stack():
    """Функция для тестирования класса Stack"""
    test_stack = Stack()

    test_stack.push(1)
    test_stack.push(2)

    assert test_stack.top.data == 2
    assert test_stack.top.next_node.data == 1
    assert test_stack.top.next_node.next_node == None

    # Перехват ожидаемой ошибки
    with pytest.raises(AttributeError):
        test_stack.top.next_node.next_node.data

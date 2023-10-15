import pytest
from src.stack import Node, Stack


@pytest.fixture
def test_stack():
    return Stack()


def test_Node():
    """Функция для тестирования класса Node"""
    test_node1 = Node(10, None)
    test_node2 = Node(20, test_node1)

    assert test_node1.data == 10
    assert test_node1.next_node is None
    assert test_node2.data == 20
    assert test_node2.next_node == test_node1


def test_Stack_push(test_stack):
    """Функция для тестирования метода push класса Stack"""
    test_stack.push(1)
    test_stack.push(2)

    assert test_stack.top.data == 2
    assert test_stack.top.next_node.data == 1
    assert test_stack.top.next_node.next_node is None

    # Перехват ожидаемой ошибки
    with pytest.raises(AttributeError):
        test_stack.top.next_node.next_node.data


def test_Stack_pop(test_stack):
    """Функция для тестирования метода pop класса Stack"""
    test_stack.push(5)
    test_stack.push(3)
    data = test_stack.pop()

    assert data == 3
    assert test_stack.top.data == 5


def test_Stack_str(test_stack):
    """Функция для тестирования метода str класса Stack"""
    test_stack.push(10)
    test_stack.push(15)

    assert str(test_stack) == "15"

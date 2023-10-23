from src.linked_list import LinkedList


def test_LinkedList():
    """Тест класса LinkedList"""
    test_data = LinkedList()

    test_data.insert_beginning({'id': 1})
    assert test_data.head.data == {'id': 1}

    test_data.insert_at_end({'id': 2})
    assert test_data.tail.data == {'id': 2}

    test_data.insert_at_end({'id': 3})
    assert test_data.tail.data == {'id': 3}

    test_data.insert_beginning({'id': 0})
    assert test_data.head.data == {'id': 0}

    test_data2 = LinkedList()

    test_data2.insert_at_end({'id': 1})
    assert test_data2.head.data == {'id': 1}

    test_data2.insert_beginning({'id': 2})
    assert test_data2.head.data == {'id': 2}


def test_test_LinkedList_str():
    """Тест метода __str__ класса LinkedList"""
    test_data = LinkedList()

    test_data.insert_beginning({'id': 1})
    test_data.insert_at_end({'id': 2})
    test_data.insert_at_end({'id': 3})
    test_data.insert_beginning({'id': 0})

    assert str(test_data) == "{'id': 0} -> {'id': 1} -> {'id': 2} -> {'id': 3} -> None"

    test_data2 = LinkedList()

    assert str(test_data2) == "None"

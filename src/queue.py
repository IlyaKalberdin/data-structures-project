class Node:
    """Класс для узла очереди"""

    def __init__(self, data, next_node):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class Queue:
    """Класс для очереди"""

    def __init__(self):
        """Конструктор класса Queue"""
        self.head = None
        self.tail = None

    def __str__(self):
        """Магический метод для строкового представления объекта"""
        str_queue_all = ""
        node = self.head

        while node is not None:
            str_queue_all += f"{str(node.data)}"
            node = node.next_node

            if node is not None:
                str_queue_all += "\n"

        return str_queue_all

    def enqueue(self, data):
        """
        Метод для добавления элемента в очередь

        :param data: данные, которые будут добавлены в очередь
        """
        node = Node(data, None)

        if self.head is None:
            self.head = node
        elif self.tail is None:
            self.tail = node
            self.head.next_node = node
        else:
            self.tail.next_node = node
            self.tail = node

    def dequeue(self):
        """
        Метод для удаления элемента из очереди. Возвращает данные удаленного элемента

        :return: данные удаленного элемента
        """
        if self.head is None:
            return None

        delete_data = self.head.data
        self.head = self.head.next_node
        return delete_data

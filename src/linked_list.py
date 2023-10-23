class Node:
    """Класс для узла односвязного списка"""
    def __init__(self, data):
        """Инициализатор экземпляра узла"""
        self.data = data
        self.next_node = None


class LinkedList:
    """Класс для односвязного списка"""
    def __init__(self):
        """Инициализатор экземпляра односвязного списка"""
        self.head = None
        self.tail = None

    def insert_beginning(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в начало связанного списка"""
        node = Node(data)

        if self.head is None:
            self.head = node
        elif self.tail is None:
            self.tail = self.head
            self.head = node
            self.head.next_node = self.tail
        else:
            node.next_node = self.head
            self.head = node

    def insert_at_end(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в конец связанного списка"""
        node = Node(data)

        if self.head is None:
            self.head = node
        elif self.tail is None:
            self.tail = node
            self.head.next_node = self.tail
        else:
            self.tail.next_node = node
            self.tail = node

    def __str__(self) -> str:
        """Вывод данных односвязного списка в строковом представлении"""
        node = self.head
        if node is None:
            return str(None)

        ll_string = ''
        while node:
            ll_string += f'{str(node.data)} -> '
            node = node.next_node

        ll_string += 'None'
        return ll_string

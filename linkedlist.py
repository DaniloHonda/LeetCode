class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_front(self, value):
        new_node = Node(value)
        if self.head:
            self.head.prev = new_node
            new_node.next = self.head  # Corrigido: Removido self.
        else:
            self.tail = new_node  # Se a lista estava vazia, tail também aponta para o novo nó.
        self.head = new_node

    def add_end(self, value):
        new_node = Node(value)
        if self.tail:
            self.tail.next = new_node
            new_node.prev = self.tail  # Corrigido: Removido self.
        else:
            self.head = new_node  # Se a lista estava vazia, head também aponta para o novo nó.
        self.tail = new_node

    def remove_front(self):
        if not self.head:  # Lista vazia
            return None

        removed = self.head.value
        self.head = self.head.next  # Avançamos para o próximo nó

        if self.head:
            self.head.prev = None  # Ajustamos o novo head
        else:
            self.tail = None  # Se a lista ficou vazia, tail também deve ser None

        return removed

    def remove_end(self):
        if not self.tail:  # Lista vazia
            return None

        removed = self.tail.value
        self.tail = self.tail.prev  # Movemos tail para o nó anterior

        if self.tail:
            self.tail.next = None  # Ajustamos o novo tail
        else:
            self.head = None  # Se a lista ficou vazia, head também deve ser None

        return removed

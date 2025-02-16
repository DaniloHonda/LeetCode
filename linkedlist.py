
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
            new_node.next = self.head
            self.head.prev = new_node
        else:
            self.tail = new_node
        self.head = new_node
        

    def add_end(self, value):
        new_node = Node(value)
        if self.tail:
            self.tail.next = new_node
            new_node.prev = self.tail
        else:
            self.head = new_node
        self.tail = new_node

    def remove_front(self, value):
        if not self.head:
            return None

        removed = self.head.value
        
        if self.head:
            self.head = self.head.next
        else:
            self.head.prev = None
        
        return removed

    def remove_end(self, value):

        if not self.tail:
            return None

        removed = self.tail.value

        if self.tail: # verifica se esta vazia ou com valor valido
            self.tail = self.tail.prev
        else:
            self.tail.next = None
        
        return removed




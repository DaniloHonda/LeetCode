class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None  # Apenas referência para o primeiro nó

    def add_front(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def remove_front(self):
        if not self.head:
            return None
        removed = self.head.value
        self.head = self.head.next
        return removed
    
    def middle(self):
        ahead = self.head
        while ahead.next and ahead:
            ahead = ahead.next.next
            self.head = ahead
        return self.head


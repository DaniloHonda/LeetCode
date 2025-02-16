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
    
    def merge(self, list1, list2):
        headtotal = Node(0)
        current = headtotal

        while list1 or list2: # Enquanto pelo menos uma das listas tiver nós
            if list1 and (not list2 or list1.value > list2.value): # Se list1 tem nó ou list2 é maior
                current.next = list2.value
                list2 = list2.next
            else:
                current.next = list1.value
                list1 = list1.next

            current = current.next

        return headtotal.next



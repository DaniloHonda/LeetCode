class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next 

def find_middle(head):
    if not head or not head.next:
        return head

    slow = head
    fast = head
    prev = None  # Para rastrear o nó antes do meio

    while fast and fast.next:
        prev = slow  # Armazena o nó anterior ao meio
        slow = slow.next
        fast = fast.next.next  

    if prev:
        prev.next = None  # Divide a lista corretamente

    return slow

def merge(l1, l2):
    head = Node()  
    tail = head
    while l1 and l2:
        if l1.val < l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    
    tail.next = l1 or l2
    return head.next

def mergesort(head):
    if not head or not head.next:
        return head
    
    middle = find_middle(head)
    right = middle
    left = mergesort(head)  # Ordena a primeira metade
    right = mergesort(right)  # Ordena a segunda metade
    
    return merge(left, right)  # Mescla as duas metades ordenadas

def print_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

# Criando a lista encadeada para teste
node1 = Node(43)
node2 = Node(2, node1)  
node3 = Node(232, node2)
node4 = Node(21, node3)
node5 = Node(21, node4)

# Ordenando a lista encadeada
sorted_list = mergesort(node5)
print_list(sorted_list)

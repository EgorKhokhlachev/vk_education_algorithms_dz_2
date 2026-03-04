class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

def find_middle(head):
    if head is None:
        return None
    
    slow = head
    fast = head
    
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    
    return slow  # возвращает первый из двух центральных при чётной длине
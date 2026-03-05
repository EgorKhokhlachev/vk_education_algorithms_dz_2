class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def merge_sorted_lists(l_1, l_2):
    d = Node(0)          
    tail = d              

    while l_1 and l_2:
        if l_1.val < l_2.val:
            tail.next = l_1
            l_1 = l_1.next
        else:
            tail.next = l_2
            l_2 = l_2.next
        tail = tail.next

    tail.next = l_1 if l_1 else l_2

    return d.next
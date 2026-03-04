class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def remove_element(head, val):
    if head is None:
        return None

    if head.value == val:
        return head.next

    # Поиск элемента для удаления
    prev = head
    current = head.next
    while current is not None:
        if current.value == val:
            # Исключаем текущий узел из списка
            prev.next = current.next
            return head  # голова не изменилась
        prev = current
        current = current.next

    # Если значение не найдено, возвращаем исходную head
    return head

def print_list(head):
    values = []
    cur = head
    while cur:
        values.append(str(cur.value))
        cur = cur.next
    print(" -> ".join(values) + " -> None")

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

print("Исходный список - ")
print_list(head)

head = remove_element(head, 3)
print("После удаления 3 - ")
print_list(head)

head = remove_element(head, 1)
print("После удаления 1 - ")
print_list(head)

head = remove_element(head, 10)
print("После попытки удалить 10 - ")
print_list(head)
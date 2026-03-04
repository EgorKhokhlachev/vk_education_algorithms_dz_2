class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def reverse_list(head):
    prev = None
    current = head
    while current is not None:
        next_node = current.next   # сохраняем следующий узел
        current.next = prev        # разворачиваем указатель
        prev = current             # сдвигаем prev вперёд
        current = next_node        # переходим к следующему узлу
    return prev                    # новая голова

# Создаём список 1 -> 2 -> 3 -> 4
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)

new_head = reverse_list(head)

# Вывод: 4 -> 3 -> 2 -> 1
node = new_head
while node:
    print(node.value, end=" -> ")
    node = node.next
# Результат: 4 -> 3 -> 2 -> 1 -> None
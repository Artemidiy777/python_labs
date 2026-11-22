class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def ll_prepend(head: Node | None, value) -> Node:
    """Добавить узел в начало и вернуть голову"""
    return Node(value, head)


def ll_from_list(values: list) -> Node | None:
    """Собрать связный список с сохранением порядка"""
    head = None
    for value in reversed(values):
        head = ll_prepend(head, value)
    return head


def ll_to_list(head: Node | None) -> list:
    """Собрать значения узлов в обычный список"""
    values = []
    current = head
    while current is not None:
        values.append(current.value)
        current = current.next
    return values


def ll_length(head: Node | None) -> int:
    """Посчитать узлы проходом от головы"""
    count = 0
    current = head
    while current is not None:
        count += 1
        current = current.next
    return count


def ll_append(head: Node | None, value) -> Node:
    """Добавить узел в конец и вернуть голову"""
    new_node = Node(value)
    if head is None:
        return new_node
    current = head
    while current.next is not None:
        current = current.next
    current.next = new_node
    return head


def ll_insert(head: Node | None, idx: int, value) -> Node:
    """Вставить узел по индексу от нуля до длины"""
    if idx < 0:
        raise IndexError('Индекс вставки вне диапазона')
    if idx == 0:
        return ll_prepend(head, value)
    current = head
    for _ in range(idx - 1):
        if current is None:
            raise IndexError('Индекс вставки вне диапазона')
        current = current.next
    if current is None:
        raise IndexError('Индекс вставки вне диапазона')
    new_node = Node(value, current.next)
    current.next = new_node
    return head


def ll_remove(head: Node | None, value) -> Node | None:
    """Удалить первое вхождение значения"""
    if head is None:
        raise ValueError('Значение не найдено')
    if head.value == value:
        return head.next
    current = head
    while current.next is not None and current.next.value != value:
        current = current.next
    if current.next is None:
        raise ValueError('Значение не найдено')
    current.next = current.next.next
    return head


def ll_reverse(head: Node | None) -> Node | None:
    """Развернуть ссылки существующих узлов"""
    prev = None
    cur = head
    while cur is not None:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt
    return prev


def ll_repr(head: Node | None) -> str:
    """Вернуть строку цепочки узлов"""
    parts = []
    current = head
    while current is not None:
        parts.append(f'[{current.value}]')
        current = current.next
    parts.append('None')
    return ' -> '.join(parts)


def ll_middle(head: Node | None) -> Node | None:
    """Найти средний узел двумя указателями"""
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    return slow


def ll_has_cycle(head: Node | None) -> bool:
    """Найти цикл алгоритмом Флойда"""
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False


def main() -> None:
    """Показать операции со связным списком"""
    head = ll_from_list([10, 20, 30])
    print('Исходный:', ll_repr(head))
    print('Как list:', ll_to_list(head))
    print('Длина:', ll_length(head))
    head = ll_prepend(head, 5)
    head = ll_append(head, 40)
    head = ll_insert(head, 2, 15)
    print('После вставок:', ll_repr(head))
    head = ll_remove(head, 15)
    print('До разворота:', ll_repr(head))
    head = ll_reverse(head)
    print('После разворота:', ll_repr(head))
    print('Средний узел:', ll_middle(head).value)
    print('Есть цикл:', ll_has_cycle(head))

    cycle_head = ll_from_list([10, 20, 30])
    cycle_head.next.next.next = cycle_head
    print('Искусственный цикл:', ll_has_cycle(cycle_head))


if __name__ == '__main__':
    main()

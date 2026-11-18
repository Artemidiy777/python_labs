from collections import deque

def stack_push(st:list, item) -> None:
    '+ эл на вершину стека'
    st.append(item)

def stack_pop(st: list):
    if not st:
        raise IndexError('Нельзя снять элемент с пустого стека')
    return st.pop()

def stack_peek(st: list):
    return st[-1] if st else None

def stack_is_empty(st: list) -> bool:
    """Проверить пустоту стека"""
    return not st

def queue_enqueue(q: deque, item) -> None:
    q.append(item)


def queue_dequeue(q: deque):
    'снять первый эл очереди'
    if not q:
        raise IndexError('нельзя снять эл с пустой очереди')
    return q.popleft()

def queue_peek(q: deque):
    """Вернуть первый элемент без удаления"""
    return q[0] if q else None

def queue_is_empty(q: deque) -> bool:
    """Проверить пустоту очереди"""
    return not q

def is_balanced(s:str) -> bool:
    st = []
    pairs = {')': '(', ']': '[', '}' : '{'}
    for char in s:
        if char in '({[':
            stack_push(st, char)
        elif char in pairs:
            if stack_is_empty(st) or stack_peek(st) != pairs[char]:
                return False
    return stack_is_empty(st)


def main() -> None:
    """Показать работу стека, очереди и задач"""
    st = []
    print('Стек пуст:', stack_is_empty(st))
    stack_push(st, 69)
    stack_push(st, 3)
    stack_push(st, 77)
    print('Стек:', st)
    print('Вершина:', stack_peek(st))
    print('Сняли:', stack_pop(st))
    print('После снятия:', st)

    q = deque()
    print('\nОчередь пуста:', queue_is_empty(q))
    queue_enqueue(q, 911)
    queue_enqueue(q, 52)
    queue_enqueue(q, 67)
    print('Очередь:', list(q))
    print('Первый:', queue_peek(q))
    print('Сняли:', queue_dequeue(q))
    print('После снятия:', list(q))

    print('\nСкобки:')
    for text in ('([]{})', '([)]', '((', '', 'x + [a * (b + c)]'):
        print(f'{text!r}: {is_balanced(text)}')
    print('\nRPN 3 4 + 2 * =', rpn('3 4 + 2 *'))


if __name__ == '__main__':
    main()



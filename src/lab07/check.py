"""ЛР7, задание C: проверка своих функций против эталона на случайных данных

Запуск: python3 -m src.lab07.check
"""

import random

from src.lab07.search import (
    binary_search,
    linear_search,
    two_sum_brute,
    two_sum_fast,
)
from src.lab07.sorting import bubble_sort, insertion_sort, selection_sort


def check_sorting(fn, trials: int = 100) -> int:
    """Сравнить сортировку fn со встроенным sorted на случайных списках
    Длины от 0 до 50, значения от -100 до 100
    Возвращает число выполненных проверок
    """
    for _ in range(trials):
        n = random.randint(0, 50)
        nums = [random.randint(-100, 100) for _ in range(n)]
        original = nums.copy()
        result = fn(nums)
        assert result == sorted(nums), f"{fn.__name__} ошиблась на {nums}: {result}"
        assert nums == original, f"{fn.__name__} изменила исходный список {original}"
    return trials


def check_search(trials: int = 100) -> int:
    """Сравнить linear_search с list.index, binary_search — на отсортированных

    Возвращает число выполненных проверок
    """
    checks = 0
    for _ in range(trials):
        n = random.randint(0, 50)
        nums = [random.randint(-20, 20) for _ in range(n)]
        x = random.randint(-20, 20)

        #list.index падает, когда числа нет
        if x in nums:
            assert linear_search(nums, x) == nums.index(x), f"linear_search на {nums}, x={x}"
        else:
            assert linear_search(nums, x) == -1, f"linear_search должен вернуть -1 на {nums}, x={x}"
        checks += 1

        ordered = sorted(nums)
        got = binary_search(ordered, x)
        if x in ordered:
            assert got != -1 and ordered[got] == x, f"binary_search на {ordered}, x={x}: {got}"
        else:
            assert got == -1, f"binary_search должен вернуть -1 на {ordered}, x={x}: {got}"
        checks += 1

        # крайние элементы списка
        if ordered:
            assert ordered[binary_search(ordered, ordered[0])] == ordered[0]
            assert ordered[binary_search(ordered, ordered[-1])] == ordered[-1]
            checks += 2

    # отдельно случаи, до которых случайные данные доходят редко
    assert binary_search([], 5) == -1, "пустой список"
    assert binary_search([5], 5) == 0, "список из одного элем"
    assert binary_search([5], 7) == -1, "один элем"
    assert binary_search([1, 3], 3) == 1, "список из двух элем"
    return checks + 4


def check_two_sum(trials: int = 100) -> int:
    """Сравнить две версии Two Sum между собой

    Пары могут не совпадать, поэтому проверяется сумма, а не индексы
    Возвращает число выполненных проверок
    """
    for _ in range(trials):
        n = random.randint(0, 30)
        nums = [random.randint(-30, 30) for _ in range(n)]
        target = random.randint(-60, 60)

        slow = two_sum_brute(nums, target)
        fast = two_sum_fast(nums, target)

        if slow is None:
            assert fast is None, f"перебор не нашёл, словарь нашёл {fast} на {nums}, target={target}"
            continue

        assert fast is not None, f"перебор нашёл {slow}, словарь нет, на {nums}, target={target}"
        for name, pair in (("two_sum_brute", slow), ("two_sum_fast", fast)):
            i, j = pair
            assert i < j, f"{name} вернула {pair}, нужно i < j"
            assert nums[i] + nums[j] == target, f"{name} вернула {pair} с суммой {nums[i] + nums[j]}"
    return trials


def main() -> None:
    random.seed(42)
    total = 0

    for fn in (bubble_sort, insertion_sort, selection_sort):
        total += check_sorting(fn)
    total += check_search()
    total += check_two_sum()

    print(f"OK: {total} проверок")


if __name__ == "__main__":
    main()

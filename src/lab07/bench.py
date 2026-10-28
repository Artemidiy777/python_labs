"""замеры времени через timeit и таблица результатов

Запуск python3 -m src.lab07.bench
"""

import random
import timeit

from src.lab04.io_txt_csv import ensure_parent_dir, write_csv
from src.lab07.search import (
    binary_search,
    linear_search,
    two_sum_brute,
    two_sum_fast,
)
from src.lab07.sorting import bubble_sort, insertion_sort, selection_sort

OUT_CSV = "data/lab07/bench.csv" # куда сохранить табл
SEED = 42            #число для генератора рандом чисел

SORT_SIZES = (1_000, 10_000, 100_000)   # размеры для мерки сортировки
QUADRATIC_LIMIT = 10_000            # выше этого квадратичные не запускать 
SEARCH_SIZE = 100_000           #длина списка для поиска
QUERIES = 10_000                # кол-ва поисков в этом списке
TWO_SUM_SIZES = (1_000, 10_000)    #на каких размерах мерить two_sum_sizes

SKIPPED = "> 60"            # метка вместо числа для слишком долгих замеров


def make_numbers(n: int) -> list[int]:
    """Список из n случайных чисел"""
    return [random.randint(-10**6, 10**6) for _ in range(n)]


def measure(fn, number: int = 1) -> float:
    """Среднее время одного вызова fn в секундах"""
    return timeit.timeit(fn, number=number) / number


def bench_sorts() -> list[tuple]:
    """Три свои сортировки против sorted на одних и тех же данных"""
    rows = []
    for n in SORT_SIZES:
        data = make_numbers(n)

        # sorted быстрый, поэтому повторяем много раз и делим
        rows.append(("sort", n, "sorted", f"{measure(lambda: sorted(data), 100):.6f}"))

        for fn in (bubble_sort, selection_sort, insertion_sort):
            name = fn.__name__.replace("_sort", "")
            if n > QUADRATIC_LIMIT:
                rows.append(("sort", n, name, SKIPPED))
                continue
            rows.append(("sort", n, name, f"{measure(lambda: fn(data)):.6f}"))
    return rows


def bench_search() -> list[tuple]:
    """Линейный против бинарного: много запросов к одному большому списку"""
    data = make_numbers(SEARCH_SIZE)
    queries = [random.choice(data) for _ in range(QUERIES)]

    rows = [(
        "search", SEARCH_SIZE, "linear",
        f"{measure(lambda: [linear_search(data, q) for q in queries]):.6f}",
    )]

    # сортировку меряем отдельной строкой: это цена подготовки к бинарному поиску
    rows.append((
        "search", SEARCH_SIZE, "sort_before_binary",
        f"{measure(lambda: sorted(data), 10):.6f}",
    ))

    ordered = sorted(data)
    rows.append((
        "search", SEARCH_SIZE, "binary",
        f"{measure(lambda: [binary_search(ordered, q) for q in queries]):.6f}",
    ))
    return rows


def bench_two_sum() -> list[tuple]:
    """перебор пар против словаря, target предпологаем, что существует"""
    rows = []
    for n in TWO_SUM_SIZES:
        nums = make_numbers(n)
        target = nums[-2] + nums[-1]        # пара лежит в самом конце списка
        rows.append(("two_sum", n, "brute", f"{measure(lambda: two_sum_brute(nums, target)):.6f}"))
        rows.append(("two_sum", n, "fast", f"{measure(lambda: two_sum_fast(nums, target), 100):.6f}"))
    return rows


def print_table(rows: list[tuple]) -> None:
    """Таблица замеров в консоль с выравниванием по колонкам"""
    print(f"{'task':<8} {'n':>8} {'impl':<20} {'seconds':>10}")
    print("-" * 50)
    last = None
    for task, n, impl, seconds in rows:
        if last is not None and (task, n) != last:
            print()
        print(f"{task:<8} {n:>8} {impl:<20} {seconds:>10}")
        last = (task, n)


def main() -> None:
    random.seed(SEED)       # фиксируем данные, чтобы замеры повторялись

    rows = bench_sorts() + bench_search() + bench_two_sum()

    print_table(rows)
    ensure_parent_dir(OUT_CSV)
    write_csv(rows, OUT_CSV, header=("task", "n", "impl", "seconds"))
    print(f"\nСохранено: {OUT_CSV}")


if __name__ == "__main__":
    main()

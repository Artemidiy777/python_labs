import timeit
from collections import deque

from src.lab04.io_txt_csv import ensure_parent_dir, write_csv
from src.lab10.linked_list import ll_prepend

SIZES = (10_000, 100_000)
OUT_CSV = 'data/lab10/bench.csv'
HEADER = ('operation', 'n', 'list_seconds', 'deque_or_ll_seconds', 'speedup')


def bench_queue(n: int) -> tuple[float, float]:
    """Измерить n удалений из начала list и deque"""
    values = list(range(n))
    q = deque(range(n))
    t_list = timeit.timeit(lambda: values.pop(0), number=n)
    t_deque = timeit.timeit(lambda: q.popleft(), number=n)
    return t_list, t_deque


def bench_prepend(n: int) -> tuple[float, float]:
    """Измерить n вставок в начало list и цепочки"""
    t_list = timeit.timeit(
        'values.insert(0, 1)',
        setup='values = []',
        number=n,
    )

    t_ll = timeit.timeit(
        'head = ll_prepend(head, 1)',
        setup='head = None',
        number=n,
        globals={'ll_prepend': ll_prepend},
    )

    return t_list, t_ll


def print_table(rows: list[tuple]) -> None:
    """Напечатать таблицу времени и ускорения"""
    print(f"{'operation':<12} {'n':>8} {'list, c':>12} {'deque/ll, c':>14} {'раз':>10}")
    print('-' * 60)
    for operation, n, t_list, t_other, speedup in rows:
        print(f'{operation:<12} {n:>8} {t_list:>12} {t_other:>14} {speedup:>10}')


def main() -> None:
    """Сравнить структуры и сохранить CSV"""
    rows = []
    for n in SIZES:
        for operation, fn in (('queue', bench_queue), ('prepend', bench_prepend)):
            t_list, t_other = fn(n)
            rows.append((
                operation, n, f'{t_list:.6f}', f'{t_other:.6f}',
                f'{t_list / t_other:.2f}',
            ))
    print_table(rows)
    ensure_parent_dir(OUT_CSV)
    write_csv(rows, OUT_CSV, header=HEADER)
    print('\nСохранено:', OUT_CSV)


if __name__ == '__main__':
    main()

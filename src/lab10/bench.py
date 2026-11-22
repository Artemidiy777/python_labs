import timeit
from collections import deque

from src.lab04.io_txt_csv import ensure_parent_dir, write_csv
from src.lab10.linked_list import ll_prepend

SIZES = (10**4, 10**5)

OUT_CSV = 'data/lab10/bench.csv'
HEADER = ('operation, n', 'list_seconds', 'deque_or_ll_seconds', 'speedup')

def bench_queue(n: int) -> tuple[float, float]:
    """Измерить n удалений из начала list и deque"""
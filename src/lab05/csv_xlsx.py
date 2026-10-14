"""ЛР5, задание B: конвертация CSV -> XLSX.

"""

import csv
from pathlib import Path
import sys

from openpyxl import Workbook
from openpyxl.utils import get_column_letter

# кладём src/ в пути поиска модулей, чтобы работали импорты из соседних лаб
SRC_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(SRC_DIR))

from lab05.json_csv import check_extension
from lab04.io_txt_csv import ensure_parent_dir



def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:
    """Преобразовать CSV в Excel

    Первая строка CSV становится заголовком таблицы, лист называется Sheet1
    Ширина колонки равна длине самого длинного текста

    Raises:
        FileNotFoundError: входного файла нет.
        ValueError: не то расширение или в CSV нет данных.
    """
    check_extension(csv_path, ".csv")
    check_extension(xlsx_path, ".xlsx")

    # читаем всё в память: csv.reader работает только с открытым файлом
    rows = []
    with Path(csv_path).open(encoding="utf-8", newline="") as f:
        for row in csv.reader(f):
            if row:
                rows.append(row)

    # одна строка -это только заголовок, записей нет
    if len(rows) < 2:
        raise ValueError("В CSV нет данных")

    wb = Workbook()
    ws = wb.active
    ws.title = "Sheet1"

    for row in rows:
        ws.append(row)

    # ищем самый длинный текст в каждой колонке
    widths = {}
    for row in rows:
        for i, value in enumerate(row, start=1):
            widths[i] = max(widths.get(i, 0), len(value))

    # Excel хранит ширину по букве колонки, а не по номеру
    for i, width in widths.items():
        ws.column_dimensions[get_column_letter(i)].width = max(width, 7)

    ensure_parent_dir(xlsx_path)
    wb.save(xlsx_path)


if __name__ == "__main__":
    # зарускать из корня проекта
    SAMPLES = "data/lab05/samples"
    OUT = "data/lab05/out"

    csv_to_xlsx(f"{SAMPLES}/people.csv", f"{OUT}/people.xlsx")
    print("people.csv -> people.xlsx")

    csv_to_xlsx(f"{SAMPLES}/cities.csv", f"{OUT}/cities.xlsx")
    print("cities.csv -> cities.xlsx")

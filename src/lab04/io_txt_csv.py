"""ЛР4, задание A: чтение текстовых файлов и запись CSV.

Модуль переиспользуемый: здесь только ввод/вывод, без подсчёта частот
и без печати в консоль
"""

import csv
from pathlib import Path


def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    """Прочитать текстовый файл целиком и вернуть его одной строкой.

    Args:
        path: путь к файлу
        encoding: кодировка файла, по умолчанию UTF-8. Если файл сохранён
            в другой кодировке, её передают явно, например:
            `read_text("data/lab04/input.txt", encoding="cp1251")`.

    Returns:
        Содержимое файла. Для пустого файла — пустая строка.

    Raises:
        FileNotFoundError: файла нет по указанному пути.
        UnicodeDecodeError: файл не читается в указанной кодировке.

    Обе ошибки намеренно не перехватываются — пусть всплывают наверх.
    файл читается целиком в память"""

    return Path(path).read_text(encoding=encoding)

def write_csv(
    rows: list[tuple | list],
    path: str | Path,
    header: tuple[str, ...] | None = None,
) -> None:
    """Записать строки в CSV-файл с разделителем-запятой.

    Существующий файл перезаписывается.

    Args:
        rows: строки таблицы; все должны быть одной длины.
        path: путь к создаваемому файлу.
        header: заголовок таблицы. Если передан, пишется первой строкой.

    Raises:
        ValueError: строки в `rows` разной длины.

    Пустой `rows` без заголовка даёт пустой файл, с заголовком —
    файл из одной строки-заголовка.
    """
    rows = [list(row) for row in rows]

    # все строки таблицы должны быть одной ширины, иначе CSV получится рваным
    if rows:
        width = len(rows[0])
        for number, row in enumerate(rows, start=1):
            if len(row) != width:
                raise ValueError(
                    f"строка {number} имеет длину {len(row)}, "
                    f"а первая строка — {width}"
                )

    # newline="" обязателен для модуля csv: перевод строки он ставит сам,
    # иначе в Windows между строками появятся пустые
    with Path(path).open("w", newline="", encoding="utf-8") as f:
        """метод .open() у объекта Path 
        - находит файл по адресу
        - если его нет, то создает
        - если уже есть, то открывает
        - возвращает новый объект(открытый файл)
        "w" (write) - файл создается, а если уже был, то обнуляется
        "a" (append) - дописывается в конце файла, содержание не трогается
        "r" (read) - только чтение
        - newline нужен, чтобы не было автоматического переноса строки, так 
          как в работе в csv он уже предусмотрен
        """
        writer = csv.writer(f)
        if header is not None:
            writer.writerow(header)
        writer.writerows(rows)                  


def ensure_parent_dir(path: str | Path) -> None:
    """Создать папку для файла, если её ещё нет.

    Нужно вызывать перед записью: `open` создаёт файл, но не папки на пути.

    Args:
        path: путь к будущему файлу (не к папке).
    """
    Path(path).parent.mkdir(parents=True, exist_ok=True)









    

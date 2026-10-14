"""ЛР5, задание A: конвертация JSON <-> CSV.

Функции только читают и пишут файлы, в консоль ничего не печатают
"""

import csv
import json
from pathlib import Path
import sys

# кладём src в пути поиска модулей, чтобы работал импорт
SRC_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(SRC_DIR))

from lab04.io_txt_csv import ensure_parent_dir


def check_extension(path: str | Path, extension: str) -> None:
    """Проверить расширение файла.

    Raises:
        ValueError: расширение не совпадает с ожидаемым.
    """
    if Path(path).suffix.lower() != extension:
        raise ValueError(f"Тип файла неверный, требуемый тип: {extension}")


def json_to_csv(json_path: str, csv_path: str) -> None:
    """Преобразовать JSON со списком словарей в CSV

    Колонки идут как в первом объекте, новые ключи дописываются в конец
    Отсутствующие поля заполняются пустой строкой

    Raises:
        FileNotFoundError: входного файла нет.
        ValueError: не то расширение, пустой файл или не список словарей.
    """
    check_extension(json_path, ".json")
    check_extension(csv_path, ".csv")

    text = Path(json_path).read_text(encoding="utf-8")

    # проверяем до json.loads: иначе пустой файл упадёт с ошибкой разбора
    if text.strip() == "":
        raise ValueError("Пустой JSON")

    data = json.loads(text)

    # not data отсекает пустой список []
    if not isinstance(data, list) or not data:
        raise ValueError("Пустой JSON или неверный тип данных")
    for item in data:
        if not isinstance(item, dict):
            raise ValueError("JSON должен быть списком словарей")

    # собираем все ключи: у разных объектов набор полей может отличаться
    columns = []
    for item in data:
        for key in item:
            if key not in columns:
                columns.append(key)

    ensure_parent_dir(csv_path)
    with Path(csv_path).open("w", newline="", encoding="utf-8") as f:
        # DictWriter раскладывает словари по колонкам по именам ключей
        writer = csv.DictWriter(f, fieldnames=columns, restval="")
        writer.writeheader()
        writer.writerows(data)
    

def csv_to_json(csv_path: str, json_path: str) -> None:
    """Преобразовать CSV в JSON со списком словарей

    Первая строка CSV — заголовок

    Raises:
        FileNotFoundError: входного файла нет

        ValueError: не то расширение, нет заголовка или нет ни одной записи
    """
    check_extension(csv_path, ".csv")
    check_extension(json_path, ".json")

    # режим по умолчанию — чтение, "w" стёр бы входной файл
    with Path(csv_path).open(encoding="utf-8", newline="") as f:
        # DictReader читает CSV как список словарей
        reader = csv.DictReader(f, restval="")

        # у пустого файла заголовка нет вообще
        if not reader.fieldnames:
            raise ValueError("В CSV отсутствует заголовок")
        
        rows = list(reader)

    if len(rows) == 0:
        raise ValueError("В CSV нет ничего кроме заголовка")

    ensure_parent_dir(json_path)
    with Path(json_path).open("w", encoding="utf-8") as f:
        json.dump(rows, f, ensure_ascii=False)


if __name__ == "__main__":
    # демонстрация сценариев, запускать из корня проекта
    SAMPLES = "data/lab05/samples"
    OUT = "data/lab05/out"

    json_to_csv(f"{SAMPLES}/people.json", f"{OUT}/people_from_json.csv")
    print("people.json -> people_from_json.csv")

    csv_to_json(f"{SAMPLES}/people.csv", f"{OUT}/people_from_csv.json")
    print("people.csv -> people_from_csv.json")

    json_to_csv(f"{SAMPLES}/students.json", f"{OUT}/students_from_json.csv")
    print("students.json -> students_from_json.csv (с пропусками полей)")

    csv_to_json(f"{SAMPLES}/cities.csv", f"{OUT}/cities_from_csv.json")
    print("cities.csv -> cities_from_csv.json")

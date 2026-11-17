import csv
from pathlib import Path

from src.lab08.models import (
    STUDENT_FIELDS,
    student_from_dict,
    update_student as update_record,
    validate_student,
)

HEADER = STUDENT_FIELDS


def ensure_storage(path: str | Path) -> None:
    """Создать CSV с заголовком, если файла нет"""
    path = Path(path)
    if not path.exists():
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open('w', encoding='utf-8', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=HEADER)
            writer.writeheader()


def load_students(path: str | Path) -> list[dict]:
    """Прочитать и проверить всех студентов"""
    ensure_storage(path)
    students = []
    with Path(path).open(encoding='utf-8', newline='') as file:
        reader = csv.DictReader(file)
        if reader.fieldnames != list(HEADER):
            raise ValueError('CSV: нужен заголовок fio,birthdate,group,gpa')
        for number, raw in enumerate(reader, start=1):
            try:
                student = student_from_dict(raw)
            except ValueError as error:
                raise ValueError(f'Запись {number}: {error}') from error
            students.append(student)
    return students


def save_students(path: str | Path, students: list[dict]) -> None:
    """Перезаписать CSV проверенными записями"""
    for student in students:
        validate_student(student)
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('w', encoding='utf-8', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=HEADER)
        writer.writeheader()
        writer.writerows(students)


def add_student(path: str | Path, student: dict) -> None:
    """Добавить студента без дубликатов по ФИО"""
    validate_student(student)
    student = student_from_dict(student)
    students = load_students(path)
    for existing in students:
        if existing['fio'] == student['fio']:
            raise ValueError('Студент с таким ФИО уже существует')
    students.append(student)
    save_students(path, students)


def list_students(path: str | Path, sort_by: str | None = None) -> list[dict]:
    """Вернуть студентов с необязательной сортировкой"""
    if sort_by not in (None, 'fio', 'gpa'):
        raise ValueError('sort_by: допустимы fio, gpa или же None')
    students = load_students(path)
    if sort_by is not None:
        students = sorted(students, key=lambda student: student[sort_by])
    return students


def find_students(path: str | Path, substr: str) -> list[dict]:
    """Найти по подстроке ФИО без учёта регистра"""
    students = load_students(path)
    query = substr.casefold()
    return [student for student in students if query in student['fio'].casefold()]


def remove_student(path: str | Path, fio: str) -> int:
    """Удалить все записи с указанным ФИО"""
    students = load_students(path)
    remaining = [student for student in students if student['fio'] != fio]
    removed = len(students) - len(remaining)
    if removed:
        save_students(path, remaining)
    return removed


def update_student(path: str | Path, fio: str, **fields) -> bool:
    """Обновить первую запись с указанным ФИО"""
    for field in fields:
        if field not in HEADER:
            raise KeyError(field)
    students = load_students(path)
    for index, student in enumerate(students):
        if student['fio'] == fio:
            students[index] = update_record(student, **fields)
            save_students(path, students)
            return True
    return False


def stats(path: str | Path) -> dict:
    """Собрать статистику студентов"""
    students = load_students(path)
    gpas = [student['gpa'] for student in students]
    groups = {}
    for student in students:
        name = student['group']
        groups[name] = groups.get(name, 0) + 1
    top = sorted(students, key=lambda student: (-student['gpa'], student['fio']))[:5]
    return {
        'count': len(students),
        'min_gpa': min(gpas) if gpas else None,
        'max_gpa': max(gpas) if gpas else None,
        'avg_gpa': sum(gpas) / len(gpas) if gpas else None,
        'groups': groups,
        'top_5_students': [
            {'fio': student['fio'], 'gpa': student['gpa']} for student in top
        ],
    }


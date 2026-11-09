import csv
import json
from datetime import date
from pathlib import Path

from src.lab08.models import (
    STUDENT_FIELDS,
    format_student,
    make_student,
    student_age,
    student_from_dict,
    student_to_dict,
    update_student,
)


def students_to_json(students: list[dict], path: str | Path) -> None:
    """Сохранить студентов в JSON"""
    data = [student_to_dict(student) for student in students]
    with Path(path).open('w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=2)


def students_from_json(path: str | Path) -> list[dict]:
    """Загрузить студентов с проверкой каждой записи"""
    with Path(path).open(encoding='utf-8') as file:
        data = json.load(file)
    if not isinstance(data, list):
        raise ValueError('В JSON ожидается массив студентов')

    students = []
    for number, raw in enumerate(data, start=1):
        try:
            student = student_from_dict(raw)
        except ValueError:
            raise ValueError(f'Запись {number} некорректна')
        students.append(student)
    return students


def students_from_csv(path: str | Path) -> list[dict]:
    """Загрузить студентов из CSV"""
    students = []
    with Path(path).open(encoding='utf-8', newline='') as file:
        reader = csv.DictReader(file)
        if reader.fieldnames != list(STUDENT_FIELDS):
            raise ValueError('CSV: нужен заголовок fio,birthdate,group,gpa')
        for number, raw in enumerate(reader, start=1):
            try:
                student = student_from_dict(raw)
            except ValueError:
                raise ValueError(f'CSV запись {number} некорректана')
            students.append(student)
    return students


def main() -> None:
    """Показать работу модели, JSON и дополнительных функций"""
    folder = Path('data/lab08')
    students = students_from_json(folder / 'students_input.json')
    print('Студенты:')
    for student in students:
        print(format_student(student))

    student = make_student('Иванов Иван Иванович', '2007-09-20', 'БИВТ-26-6-1', 4.3)
    print('Возраст до дня рождения:', student_age(student, date(2026, 9, 19)))
    print('Возраст в день рождения:', student_age(student, date(2026, 9, 20)))
    print('Копия — отдельный словарь:', student_to_dict(student) is not student)

    output = folder / 'students_output.json'
    students_to_json(students, output)
    restored = students_from_json(output)
    print('\nСохранено:', output)
    print('JSON туда-обратно, данные совпали:', restored == students)
    print('GPA второй записи после загрузки:', restored[1]['gpa'])

    print('\nПроверка ошибок:')
    try:
        students_from_json(folder / 'students_bad.json')
    except ValueError:
        print('Неверная дата')
    try:
        make_student('Иванов Иван', '2007-05-14', 'БИВТ-26-6-1', 7)
    except ValueError:
        print('GPA 7',)

    updated = update_student(student, gpa=4.8)
    csv_students = students_from_csv(folder / 'students.csv')
    print('\nЗадания со звёздочкой:')
    print('Исходный GPA:', student['gpa'], '| Новый GPA:', updated['gpa'])
    print('После обновления словари разные:', updated is not student)
    print('Прочитано из CSV:', len(csv_students))
    print('Тип GPA из CSV:', type(csv_students[0]['gpa']).__name__)


if __name__ == '__main__':
    main()

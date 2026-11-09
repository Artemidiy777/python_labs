from datetime import date

STUDENT_FIELDS = ("fio", "birthdate", "group", "gpa")


def validate_student(rec: dict) -> None:
    """Проверить поля и значения записи"""
    if not isinstance(rec, dict):
        raise ValueError('student должен быть словарем')
    
    if set(rec) != set(STUDENT_FIELDS):
        raise ValueError('нужны ровно поля fio, birthdate, group, gpa')
    
    for field in ('fio', 'group'):
        value = rec[field]
        if not isinstance(value, str) or not value.strip():
            raise ValueError(f'{field}: требуется непустая строка')
        
    birthdate = rec['birthdate']
    if not isinstance(birthdate, str):
        raise ValueError('birthdate требует формат YYYY-MM-DD')
    
    try:
        birthday = date.fromisoformat(birthdate)
    except ValueError:
        raise ValueError('birthdate: несуществующая дата или неверный формат')
    
    if birthday.isoformat() != birthdate:
        raise ValueError('birthdate нужен формат YYYY-MM-DD')
    
    if birthday > date.today():
        raise ValueError('birthdate: дата рождения из будущего')

    gpa = rec['gpa']
    if isinstance(gpa, bool) or not isinstance(gpa, (int, float)):
        raise ValueError('в gpa требуется число, булевое значение не подходит')
    if not (0 <= gpa <= 5):
        raise ValueError('gpa: требуется значение от 0 до 5')


def make_student(fio, birthdate, group, gpa) -> dict:
    """Создать проверенную запись студента"""
    rec = {
        "fio": fio,
        "birthdate": birthdate,
        "group": group,
        "gpa": gpa,
    }

    validate_student(rec)
    rec['fio'] = fio.strip()
    rec['group'] = group.strip()
    rec['gpa'] = float(gpa)
    return rec


def student_age(rec: dict, today: date | None = None) -> int:
    """Посчитать полные годы на указанную дату"""
    validate_student(rec)
    if today is None:
        today = date.today()
    birthday = date.fromisoformat(rec['birthdate'])
    age = today.year - birthday.year
    if (today.month, today.day) < (birthday.month, birthday.day):
        age -= 1
    return age


def format_student(rec: dict) -> str:
    """Вернуть ФИО с инициалами, группу, возраст и GPA"""
    age = student_age(rec)
    parts = rec['fio'].split()
    initials = ''
    for part in parts[1:]:
        initials += part[0].upper() + '.'
    short_name = parts[0]
    if initials:
        short_name += ' ' + initials
    return f"{short_name} ({rec['group'].strip()}), {age} лет, GPA {rec['gpa']:.2f}"


def student_to_dict(rec: dict) -> dict:
    """Вернуть проверенную копию записи"""
    validate_student(rec)
    return rec.copy()


def student_from_dict(d: dict) -> dict:
    """Преобразовать внешний словарь в запись студента"""
    if not isinstance(d, dict):
        raise ValueError('student должен быть словарем')
    if set(d) != set(STUDENT_FIELDS):
        raise ValueError('нужны ровно поля fio, birthdate, group, gpa')

    raw_gpa = d['gpa']
    if isinstance(raw_gpa, bool) or not isinstance(raw_gpa, (str, int, float)):
        raise ValueError('gpa: требуется число или числовая строка')
    try:
        gpa = float(raw_gpa)
    except (ValueError, OverflowError) as error:
        raise ValueError('gpa: не удалось преобразовать значение в число') from error
    return make_student(d['fio'], d['birthdate'], d['group'], gpa)


def update_student(rec: dict, **fields) -> dict:
    """Вернуть новую запись с изменёнными полями"""
    validate_student(rec)
    for field in fields:
        if field not in STUDENT_FIELDS:
            raise KeyError(field)

    updated = rec.copy()
    updated.update(fields)
    return make_student(
        updated['fio'], updated['birthdate'], updated['group'], updated['gpa']
    )
    

def format_record(rec):
    fio, group, gpa = rec
    
    if not isinstance(fio, str) or not isinstance(group, str):
        raise TypeError("ФИО и группа должны быть строками")
    if not isinstance(gpa, (int, float)):
        raise TypeError("GPA должен быть числом")
    
    parts = fio.split()
    if len(parts) <= 1:
        raise ValueError("ФИО должно содержать хотя бы фамилию и имя")
    
    group = group.strip()
    if not group:
        raise ValueError("группа не может быть пустой")
    
    surname = parts[0].capitalize()
    initials = ''.join(p[0].upper() + '.' for p in parts[1:])
    
    return f"{surname} {initials}, гр. {group}, GPA {gpa:.2f}"

fio = input("Введите ФИО: ")
group = input("Введите группу: ")
gpa = float(input("Введите GPA: "))

rec = (fio, group, gpa)
print(format_record(rec))

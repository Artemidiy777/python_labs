name = input('Ваше ФИО: ')
name = name.split()

if len(name) != 3:
    print('Нужно ввести три слова: фамилию, имя и отчество')
else:
    initials = f'{name[0][0]}{name[1][0]}{name[2][0]}.'
    total_length = len(name[0]) + len(name[1]) + len(name[2])
    print(f'''Инициалы: {initials}
Длина (символов): {total_length}''')

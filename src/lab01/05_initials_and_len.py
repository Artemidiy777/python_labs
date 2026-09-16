name_input = input('Ваше ФИО: ')
name = name_input.split()

if len(name) != 3:
    print('Нужно ввести три слова: фамилию, имя и отчество')
else:
    initials = f'{name[0][0]}{name[1][0]}{name[2][0]}.'
    total_length = len(name_input)
    print(f'''Инициалы: {initials}
Длина (символов): {total_length}''')
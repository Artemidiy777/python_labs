name_input = input('Ваше ФИО: ')
name = name_input.split()

if len(name) != 3:
    print('Нужно ввести три слова: фамилию, имя и отчество')
else:
    initials = f'{name[0][0].upper()}{name[1][0].upper()}{name[2][0].upper()}.'
    
    letters_length = len(name[0]) + len(name[1]) + len(name[2])
    spaces_count = len(name) - 1
    total_length = letters_length + spaces_count
    
    print(f'''Инициалы: {initials}
Длина (символов): {total_length}''')
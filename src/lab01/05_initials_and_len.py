name = input('Ваше ФИО: ')
name = name.split()
print(f'''Инициалы: {name[0][0]}{name[1][0]}{name[2][0]}
Длина (символов): {len(name[0])+len(name[1])+len(name[2])}''')

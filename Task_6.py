""" Задание №6. Пользователь вводит номер буквы в алфавите. Определить, какая это буква. """

number_letter = int(input('Здравствуйте, введите порядковый номер буквы в русском алфавите: '))
number_list = [chr(p) for p in range(ord('А'), ord('Я') + 1)]
if number_letter < len(number_list) + 1:
    print(f'Введенный Вами порядковый номер буквы в русском афлавите {number_letter}'
          f' представляет собой букву {number_list[number_letter - 1]} (в верхнем регистре)')
else:
    print('Ошибка! В русском алфавите всего 32 буквы! Введите заново порядковый номер буквы в русском алфавите!')


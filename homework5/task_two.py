user_index = int(input('Введите индекс: '))

a = 0
b = 1
index = 1
while True:
    index += 1
    new_number = a + b
    a = b
    b = new_number

    if user_index == index:
        print(f'Пользователь ввёл индекс {index} ')
        print(f'Результат: число Фибоначчи = {new_number}')
        print()
        print(f'Пользователь ввёл число {new_number}')
        print(f'Результат: число Фибоначчи = {new_number}')

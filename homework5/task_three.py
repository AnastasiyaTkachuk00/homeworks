text = open('test.txt')
string = input('Введите букву:')
letter = 0
for i in text:
    if i.isalpha():
        letter += 1
print('Результат: буква встречается', letter, 'раз в тексте')
text.close()

# Вариант - 5

# Дано целое число N (1 < N < 26).
# Вывести N последних строчных (то есть маленьких)
# букв латинского алфавита в обратном порядке (начиная с буквы «z»).

textToPrint = 'Введите целое число N, которое 1 < n < 26: '
n = input(textToPrint)

#Исключение для ввода
while type(n) != int:
    try:
        n = int(n)
        if n < 1:
            print('Введено число, которое меньше 1!')
            n = input(textToPrint)
        elif n > 26:
            print('Введено число, которое больше 26!')
            n = input(textToPrint)
    except ValueError:
        print('Введено не целое число!')
        n = input(textToPrint)

# Цикл с последующим выводом данных
for i in range(n):
    print(chr(ord('z') - i), end = ' ')

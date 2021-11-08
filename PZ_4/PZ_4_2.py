# Вариант - 5
# Дано вещественное число — цена 1 кг конфет.
# Вывести стоимость 1.2, 1.4, ..., 2 кг конфет.

#Проверка исключения
num = input("Введите целое число: ")
while type(num) != int:
    try:
        num = int(num)
    except ValueError:
       print('Введено число!')
       num = input('Введите число: ')

#Ввод переменных
sum = 0
count = 0

while num > 0:
    fra = num % 10
    sum += fra
    num = num // 10
    count += 1

print("Сумма цифр: ", sum)
print("Количество цифр: ", count)
# Вариант - 5
# Дано вещественное число — цена 1 кг конфет.
# Вывести стоимость 1.2, 1.4, ..., 2 кг конфет.

#Проверка исключения
val = input("Введите вещественное число: ")
while type(val) != float:
    try:
        val = float(val)
    except ValueError:
       print('Введено не число!')
       val = input('Введите вещественное число: ')

#Ввод переменных
i = 0
kg = 1
while i <= 5:
    #Форматирование числа
    print('{0:.1f} кг стоит {1:.1f}'.format(round(kg, 2), round(kg * val, 2)))
    i += 1
    kg += 0.2

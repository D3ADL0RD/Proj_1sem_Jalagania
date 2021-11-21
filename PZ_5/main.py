#Вариант - 5

#С помощью функций получить вертикальную и горизонтальную линии.
#Линия проводится многократной печатью символа.
#Заключить слово в рамку из полученных линий.

#Создание из символа горизонтальной линии
def horizontalLine(count):
    return '-' * (count + 4)

#Создание двух вертикальных символов и последующие заключение в них текста
def verticalLine(text):
    return ('| {} |').format(text)

#Ввод значений и создание переменных
text = str(input('Введите текст: '))
textLen = len(text)
horLine = horizontalLine(textLen)
verLine = verticalLine(text)

#Вывод результатов
print(horLine)
print(verLine)
print(horLine)
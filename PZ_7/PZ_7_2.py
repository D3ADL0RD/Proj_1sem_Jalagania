# Вариант - 5

# Дана строка-предложение на русском языке и число K (0 < K < 10).
# Зашифровать строку, выполнив циклическую замену каждой буквы на букву того же регистра,
# расположенную в алфавите на K-й позиции после шифруемой буквы (например, для
# K = 2 «А» перейдет в «В», «а» — в «в», «Б» — в «Г», «я» — в «б» и т. д.).
# Букву «ё» в алфавите не учитывать, знаки препинания и пробелы не изменять.

def convert(s):
    str1 = ""
    return (str1.join(s))

text = list(input('Введите текст: '))

textLen = len(text)

textToPrint = 'Введите число, которое будет больше нуля, но меньше десяти! \n'
k = input(textToPrint)

#Исключение для ввода
while type(k) != int:
    try:
        k = int(k)
        if k < 0:
            print('Введено число, которое меньше нуля!')
            k = input(textToPrint)
        elif k > 10:
            print('Введено число, которое больше десяти!')
            k = input(textToPrint)
    except ValueError:
        print('Введено не целое число!')
        k = input('Введите число: ')

exceptionList = [' ', ',', '.', '?', '!', '"', "'", ":", ';', '/', '-', '_', '(', ')', '{', '}', '[', ']']

for i in range(0, textLen):
    if text[i] == 'Ё':
        text[i] = 'Е'

    if text[i] == 'ё':
        text[i] = 'е'

    if text[i] not in exceptionList:
        block = False

        ordValue = ord(text[i])

        if ordValue + k >= 1103:
            text[i] = chr(1071 + k)
            block = True

        if ordValue <= 1071 and ordValue + k > 1071:
            text[i] = chr(1039 + k)
            block = True

        if block == False:
            text[i] = chr(ordValue + k)

print(convert(text))
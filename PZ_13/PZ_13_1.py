# Вариант - 5
# Из последовательности на n целых чисел создать новую последовательность, в
# которой каждый последующий элемент равен квадрату суммы двух соседних элементов.
n = 10
firstTable = [i for i in range(n)]

secondTable = []

print('До: ', firstTable)

resultLambda = lambda i: i + 1 in firstTable and i + 2 in firstTable and pow(i + 1, 2) + pow(i + 2, 2)

for i in firstTable:
    if (i + 1 and i + 2) in firstTable:
        secondTable.append(resultLambda(i))

print('После:', secondTable)
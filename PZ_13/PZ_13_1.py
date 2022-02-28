# Вариант - 5
# Из последовательности на n целых чисел создать новую последовательность, в
# которой каждый последующий элемент равен квадрату суммы двух соседних элементов.
n = 10
nT = []

i = 0
while i <= n:
    nT.append(i)
    i += 1

iVal1 = lambda iVal1: iVal1 in nT and pow(iVal1, 2)
iVal2 = lambda iVal2: iVal2 in nT and pow(iVal2, 2)

iVal = lambda x, y: x in nT and y in nT and pow(x, 2) + pow(y, 2)

for i in nT:
    res = iVal(i - 1, i - 2)
    if res != False:
        print(i, res)
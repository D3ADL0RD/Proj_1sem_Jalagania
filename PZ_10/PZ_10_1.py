# Вариант-5
# Средствами языка Python сформировать текстовый файл (.txt),
# содержащий последовательность из целых положительных и отрицательных чисел.
# Сформировать новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую обработку элементов:
#
# Исходные данные:
# Количество элементов:
# Сумма элементов:
# Элементы, умноженные на минимальный элемент:

def multiply(lst):
    answer = 0
    for i in lst:
        answer += i
    return answer

def multiply2(lst, exp):
    tbl = []
    for i in lst:
        tbl.append(i * exp)
    return tbl


l = '-4 92 3 10 -28 -1 33 -4'
f1 = open('new_file_1.txt', 'w')
f1.writelines(l)
f1.close()

f2 = open('new_file_2.txt', 'w', encoding='UTF-8')
f2.write('Исходные данные: ')
f2.writelines(l)
f2.write('\n')
f2.close()

f1 = open('new_file_1.txt')
k = f1.read()
k = k.split()
c = str(len(k))
f1.close()

l = [-4, 92, 3, 10, -28, -1, 33, -4]
f2 = open('new_file_2.txt', 'a', encoding='UTF-8')
f2.write('Количество элементов: ')
f2.writelines(c)
f2.write('\n')
f2.write('Сумма элементов: ')
rVal = multiply(l)
f2.writelines(str(rVal))
f2.write('\n')
f2.write('Элементы, умноженные на минимальный элемент: ')
lNew = l.copy()
lNew.sort()
minVal = lNew[0]
f2.writelines(str(multiply2(l, minVal)))
f2.write('\n')
f2.close()
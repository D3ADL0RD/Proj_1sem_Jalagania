# Вариант-5

# Дан список A размера N и целые числа K и L (1 < K < L < N).
# Переставить в обратном порядке элементы списка,
# расположенные между элементами AK и AL, включая эти элементы.

n = input('Введите целое число N: ')

#Исключение для вводиммых переменных
while type(n) != int:
    try:
        n = int(n)
        if n < 1:
            print('Введено число, которое меньше 1!')
            n = input('Введите целое число N: ')
    except ValueError:
        print('Введено не целое число!')
        n = input('Введите целое число N: ')

l = input("Введите целое число L: ")

while type(l) != int:
    try:
        l = int(l)
        if l > n:
            print('Введено число, которое больше N!')
            l = input('Введите целое число L: ')
    except ValueError:
        print('Введено не целое число!')
        l = input('Введите целое число L: ')

k = input("Введите целое число K: ")

while type(k) != int:
    try:
        k = int(k)
        if k >= l:
            print('Введено число, которое больше L!')
            k = input('Введите целое число K: ')
    except ValueError:
        print('Введено не целое число!')
        k = input('Введите целое число K: ')

# Пустая таблица, в которой сгенерериуется
# список чисел до переменной N
tbl = []
i = 0
while i < n:
    i += 1
    tbl.append(i)

print('До ', tbl)

# Функция перестановки элементов списка
n1Index = tbl.index(k)
n2Index = tbl.index(l) + 1
n1Index, n2Index = min(n1Index, n2Index), max(n1Index, n2Index)
tbl = tbl[0:n1Index]+tbl[n1Index:n2Index][::-1]+tbl[n2Index:]
print('После ', tbl)
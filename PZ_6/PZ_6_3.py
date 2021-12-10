# Вариант - 5

# Дан список размера N.
# Обнулить все его локальные максимумы
# (то есть числа, большие своих соседей).

from random import randrange

# Ввод целого числа
n = int(input('Введите целое число N: '))

# Таблица со случайными значениям длиной N
tbl = [randrange(1, 21) for i in range(n)]
print('До ', tbl)

# Приравнивание к нулю локального максимума
if tbl[0] > tbl[1]:
    i = 2
else
    i = 1
    for i in range(1, n - 1):
        if tbl[i-1] < tbl[i] and tbl[i] > tbl[i+1]:
            tbl[i] = 0

# Вывод
print('После ', tbl)
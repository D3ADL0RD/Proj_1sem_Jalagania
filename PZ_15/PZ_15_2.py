# Вариант - 5
# Сгенерировать матрицу, в которой нечетные элементы заменяются на 0.

from random import randint

matrix = [[randint(1, 11) for j in range(3)] for i in range(3)]

print('До:', matrix)

mathPow = lambda index, key, value: value % 2 != 0 and (matrix[index].insert(key, 0), matrix[index].remove(value))

for k, v in enumerate(matrix):
    for k1, v1 in enumerate(v):
        mathPow(k, k1, v1)

print('После:',matrix)
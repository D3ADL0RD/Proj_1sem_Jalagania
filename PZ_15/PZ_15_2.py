# Вариант - 5
# Сгенерировать матрицу, в которой нечетные элементы заменяются на 0.
from random import randint

width, heigth = int(input('Введите ширину матрицы: ')), int(input('Введите длину матрицы: '))

matrix = [[randint(-3, 3) for j in range(width)] for i in range(heigth)]

print('До:', matrix)

res = lambda value: value % 2 != 0

for k, v in enumerate(matrix):
    for k1, v1 in enumerate(v):
        if res(v1):
            matrix[k][k1] = 0

print('После:',matrix)
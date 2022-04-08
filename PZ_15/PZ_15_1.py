# Вариант - 5
# В матрице элементы второго столбца возвести в квадрат.
from random import randint

width, heigth = int(input('Введите ширину матрицы: ')), int(input('Введите длину матрицы: '))

matrix = [[randint(1, 6) for j in range(width)] for i in range(heigth)]
print('До:', matrix)

math_pow = lambda key, value: key == 1 and pow(value, 2)

for k, v in enumerate(matrix):
    for k1, v1 in enumerate(v):
        res = math_pow(k1, v1)
        if res:
            matrix[k][k1] = res

print('После:',matrix)

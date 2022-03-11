# Вариант - 5
# В матрице элементы второго столбца возвести в квадрат.

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print('До:', matrix)

mathPow = lambda index, key, value: key == 1 and (matrix[index].insert(key, pow(value, 2)), matrix[index].remove(value))

for k, v in enumerate(matrix):
    for k1, v1 in enumerate(v):
        mathPow(k, k1, v1)

print('После:',matrix)

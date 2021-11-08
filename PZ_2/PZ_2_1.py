# Вариант 5
# Дана скорость первой машины, скорость второй машины,
# расстояние между машинами и время
# Определить расстояние между ними через время, если автомобили удаляются друг от
# друга.

try:
    v1 = int(input('\nВведите скорость первого автомобиля: '))
    v2 = int(input('\nВведите скорость второго автомобиля: '))
    d = int(input('\nВведите расстояние между автомобилем: '))
    T = int(input('\nВведите время: '))

    # Результат сложений всех переменных
    res = abs(d - (v1 + v2) * T)

    print('\nРасстояния между ними через T-часов будет равно: {}'.format(res))
except ValueError:
    print('\nЧто-то пошло не так, введите целое число')
# Разработать программу с применением пакета tk, взяв в качестве условия одну
# любую задачу из ПЗ №№ 3 – 8.
# Задача взята из ПЗ 4-2
# Дано целое число N (>0). Используя операции деления нацело
# и взятия остатка от деления, найти количество и сумму его цифр.

import tkinter as tk
def result():
    num = int(s1.get())
    sum = 0
    count = 0

    while num > 0:
        fra = num % 10
        sum += fra
        num = num // 10
        count += 1

    res.config(text='Сумма цифр - {}, количество цифр - {}'.format(sum, count))


root = tk.Tk()
root.geometry('500x500')
root.title('PZ_12_2')
res = tk.Label(root, text='Введите целое положительное число:')
res.pack()
s1 = tk.Entry(root)
s1.pack()
button = tk.Button(root, text='Подсчитать сумму цифр и их количество', command=result)
button.pack()
res = tk.Label(root, text='Результат:')
res.pack()

root.mainloop()
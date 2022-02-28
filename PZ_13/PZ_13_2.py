# Вариант - 5
# Составить генератор (yield), который переведет символы строки из нижнего
# регистра в верхний.

def lower_to_upper(str):
    for ch in str:
        yield ch.upper()


string = input("Введите произвольные символы нижнего регистра: ")
print(''.join(lower_to_upper(string)))

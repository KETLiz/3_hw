# 4'. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# *Пример:*
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

a = int(input('Введите число: '))
while a != 0:
    res = a%2
    a = a // 2
    print(res)

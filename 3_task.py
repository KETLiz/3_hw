# 3'. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу 
# между максимальным и минимальным значением дробной части элементов.
# *Пример:*
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

list = [1.1, 1.2, 3.1, 5, 10.01]

# res = " ".join([str(i) for i in list])
a, b, c, d, e = list

a1 = a - int(a)
b1 = b - int(b)
c1 = c - int(c)
d1 = d - int(d)
e1 = e - int(e)

li = []
li.append(round(a1, 3))
li.append(round(b1, 3))
li.append(round(c1, 3))
li.append(round(d1, 3))
li.append(round(e1, 3))

print(li)
result_li = [i for i in li if type(i)!= int]
print(result_li)
max_number = max(result_li)
min_number = min(result_li)
print(f'Разница между максимальным и минимальным значением дробной части массива равна {max_number-min_number}')
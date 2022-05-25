from datetime import datetime

start_time = datetime.now()
a = list(input("Число: "))  # вводим число
len = len(a)  # получаем длинну списка
x = int(len / 2)
b = a
c = (sorted(list(a[:x])))  # сортируем первую половину
d = (sorted(list(b[x:])))  # сортируем вторую половину
# print(c)
# print(d)
print(sorted(list(c + d)))
# print(sorted(a))
print(datetime.now() - start_time)

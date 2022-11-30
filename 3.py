# Реализуйте алгоритм перемешивания списка. Встроенный алгоритм SHUFFLE не использовать! Реализовать свой метод

from random import randint as rnd

size = int(input('Введите размер списка: '))
rnd_list = []
for i in range(size):
    rnd_list.append(rnd(100, 999))


print ("Начальный список: " + str(rnd_list))
for i in range(len(rnd_list)-1, 0, -1):
    j = rnd(0, i + 1)
    rnd_list[i], rnd_list[j] = rnd_list[j], rnd_list[i]
print ("Перемешанный список: " +  str(rnd_list))
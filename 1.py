# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

num = input('Введите число: ')

def summ(num):
    number = 0
    for i in str(num):
        if i != '.':
            number += int(i)
    return number


print(f'Сумма цифр числа равна {summ(num)}')

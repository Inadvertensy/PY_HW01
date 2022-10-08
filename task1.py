"""
Напишите программу, которая принимает на вход цифру,
обозначающую день недели, и проверяет, является ли этот день выходным.

Пример:

- 6 -> да
- 7 -> да
- 1 -> нет
"""
print('Please enter weekday')
N = int(input('Введите \nN: '))

if N == 1 or N == 2 or N == 3 or N == 4 or N == 5:
    print('weekday')
elif N == 6 or N == 7:
    print('weekend')
else:
    print('Number you have entered is not day number')

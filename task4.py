"""
Напишите программу, которая по заданному номеру четверти,
показывает диапазон возможных координат точек в этой четверти (x и y).
"""

q = int((input('Please enter \nquarter number: ')))
if q == 1:
    print('x>0, y>0')
elif q == 2:
    print('x<0, y>0')
elif q == 3:
    print('x<0, y<0')
elif q == 4:
    print('x>0, y>0')
else:
    print('Number you have entered is not a quarter number')

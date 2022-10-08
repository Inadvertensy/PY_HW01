"""
Напишите программу, которая принимает на вход координаты двух
точек и находит расстояние между ними в 2D пространстве.

Пример:

- A (3,6); B (2,1) -> 5,09
- A (7,-5); B (1,-1) -> 7,21
"""
import math

XA = int((input('Please enter \nA coordinate X: ')))
YA = int((input('Please enter \nA coordinate Y: ')))
XB = int((input('Please enter \nB coordinate X: ')))
YB = int((input('Please enter \nB coordinate Y: ')))
# d = √ (х А – х В) 2 + (у А – у В) 2
result = ((XB - XA) ** 2) + ((YB - YA) ** 2)
sqrt = math.sqrt(result)
print(round(sqrt, 3))

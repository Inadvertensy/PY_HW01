"""
Напишите программу для. проверки истинности утверждения
¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

"""
for x in range(0, 2):

    for y in range(0, 2):

        for z in range(0, 2):
            print(x, y, z)
            print((~ (x | y | z)) == (~ x & ~ y & ~ z))
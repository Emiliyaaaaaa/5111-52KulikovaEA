# Используем библиотеку математики
import math
# Создание лямбда-функции расчёта длины гипотенузы
hypotenuse = lambda x, y: math.sqrt(x*x + y*y)
a = int(input("Введите длину первого катета "))
b = int(input("Введите длину второго катета "))
print(hypotenuse(a, b))



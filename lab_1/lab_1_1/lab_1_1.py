from math import *
a=int(input('Введите длину первой стороны треугольника: '))
b=int(input('Введите длину второй стороны треугольника: '))
c=int(input('Введите длину третьей стороны треугольника: '))
p=(a+b+c)/2

if a+b<=c or a+c<=b or c+b<=a:
    print("Такого треугольника не существует")
else:
    s = sqrt(p * (p - a) * (p - b) * (p - c))
    g  =round(s,2)
    print (g)

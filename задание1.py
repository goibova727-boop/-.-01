import math

a = float(input("Введите сторону a: "))
b = float(input("Введите сторону b: "))
c = float(input("Введите сторону c: "))

# Полупериметр
p = (a + b + c) / 2

# Площадь по формуле Герона
area = math.sqrt(p * (p - a) * (p - b) * (p - c))

print(f"Площадь треугольника: {area:.2f}")

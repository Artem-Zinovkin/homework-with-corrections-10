# конвертация градусов в радианы и наоборот
import math

while True:
    def degrees(a):
        return round((a * math.pi) / 180, 5)


    def radians(a):
        return round((a * 180) / math.pi, 5)


    d = float(input("из градусов в радианы нажмите (1)   из радиан в градусы нажмите (2) \n сделайте свой выбор  "))
    if d == 1:
        b = degrees(a=float(input("Введите число в градусах ")))
        print(F"число в радианах = {b} ")
    elif d == 2:
        с = radians(a=float(input("Введите число в радианах ")))
        print(F"число в градусах = {с} ")
    else:
        break
print('некорректный ввод, введите (1) или (2)')

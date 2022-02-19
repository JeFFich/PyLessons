def task1():
    s1 = input("Идет ли дождь? \n").lower()
    if (s1 == "yes"):
        s2 = input("Ветрено ли на улице? \n").lower()
    if (s1 == "yes"):
        if (s2 == "yes"):
            print("It is too windy for an umbrella \n")
        else:
            print("Take an umbrella \n")
    else:
        print("Enjoy your day \n")

task1()

def task2():
    print(input("Введите ваше имя: \n").title(),
          input("Введите вашу фамилию: \n").title())

task2()

def task3():
    s = input("Введите первую строку стихотворения: \n")
    print(len(s))
    st = int(input("Введите начальную позицию: \n"))
    fin = int(input("Введите конечную позицию: \n"))
    if (0 <= st < len(s)) and (0 <= fin < len(s)) and (st < fin):
        print(s[st: fin])
    else:
        print("Введённые позиции неправильны")

task3()

def task4():
    s = input("Введите ваше имя: \n")
    if (len(s) < 5):
        s1 = input("Длина введеного имени слишком маленькая! Введите еще и фамилию: \n")
        print((s + s1).upper())
    else:
        print(s.lower())

task4()
        
from math import sqrt as sqr
def task5():
    k = int(input("Введите целое число, большее 500: \n"))
    print(round(sqr(k), 2))

task5()

from math import pi as P
def task6():
    s = input("Введите тип фигуры: \n").lower()
    if (s == "круг") or (s == "треугольник") or (s == "прямоугольник"):
        if (s == "круг"):
            r = int(input("Введите радиус круга: \n"))
            print(f"Площадь круга: {round(P * r**2, 2)}")
        elif (s == "треугольник"):
            a = int(input("Введите длину стороны А: \n"))
            b = int(input("Введите длину стороны B: \n"))
            c = int(input("Введите длину стороны C: \n"))
            p1 = (a + b + c)/2
            print(f"Площадь треугольника: {round(sqr(p1 * (p1 - a) * (p1 - b) * (p1 - c)), 2)}")
        else:
            a = int(input("Введите длину стороны А: \n"))
            b = int(input("Введите длину стороны B: \n"))
            print(f"Площадь прямоугольника: {round(a * b, 2)}")
    else:
        print("Введеные данные не соответствуют условиям задачи!")

task6()

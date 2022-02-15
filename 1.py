def task1():
    print(f'Площадь комнаты: {round(float(input("Введите длину комнаты: ")) * float(input("Введите ширину комнаты: ")), 10)}')

task1()

def task2():
    a = int(input("Введите первое число: "))
    b = int(input("Введите второе число: "))
    print(f'{a} в степени {b} равно {pow(a, b)}, {b} в степени {a} равно {pow(b, a)}')

task2()

def task3():
    a = int(input("Введите первое число: "))
    b = int(input("Введите второе число: "))
    c = int(input("Введите третье число: "))
    print('The answer is ', (a + b) * c)

task3()

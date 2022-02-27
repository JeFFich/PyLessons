from random import randint as random

c = random(1, 10)
while True:
    k = int(input("Введите целое число от 1 до 10: \n"))
    if (k == c):
        print("Вы угадали!")
        break
    elif (k < c):
        print("Введённое число меньше загаданного")
    else:
        print("Введённое число больше загаданного")

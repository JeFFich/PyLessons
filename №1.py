def result(a, op):
    try:
        c1 = float(a[0])
        c2 = float(a[1])
        if (op == "+"):
            return c1 + c2
        elif (op == "-"):
            return c1 - c2
        elif (op == "/"):
            return c1/c2
        else:
            return "Операция отсутствует"
    except ValueError:
        return "Ошибка преобразования типов"
    except ZeroDivisionError:
        return "Ошибка деления на ноль"

s = input("Введите два числа: \n")
operation = input("Введите операцию: \n")
print(result(s.split(" "), operation))

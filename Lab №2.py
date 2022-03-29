def getdata():
    file = open('students.txt', 'r')
    data = [i for i in file.read().split("\n") if (i != "")]
    file.close()
    return data

def writedata(data):
    file = open('students.txt', 'w')
    for line in data:
        file.write(line + "\n")
    file.close()


def add(stud):
    data = getdata()
    if not(stud in data):
        data.append(stud)
        writedata(sorted(data))
        return "Студент успешно добавлен!"
    else:
        return "Студент " + stud + " уже есть в списке!"


def seek(student):
    data = getdata()
    if (len(student) == 1):
        surnames = list(map(lambda x: x.split()[0], data))
        try:
            flag = surnames.index(student[0])
            return "Студенты со схожей фамилией: " + ", ".join([data[i] for i in range(flag, flag + surnames.count(student[0]))])
        except ValueError:
            return "Студентов с такой фамилией нет в группе"
    elif (len(student) == 2):
        return "Данный студент находится в группе" if ((student[0] + ' ' + student[1]) in data) else "Данного студента в группе нет"
    else:
        return "Неправильный формат введённых данных"


def change(stud, sur=None, name=None):
    data = getdata()
    if (stud in data):
        data.remove(stud)
        data.append(" ".join([sur if sur else stud.split()[0], name if name else stud.split()[1]]))
        writedata(sorted(data))
        return "Данные о студенте успешно изменены"
    else:
        return "Данного студента в группе нет"


def removal(sur, name=None):
    data = getdata()
    if not(name):
        res = seek([sur])
        if (res == "Студентов с такой фамилией нет в группе"):
            print(res)
        else:
            name = input(res + "\nВведите имя одного студента из списка\n")
            removal(sur, name = name)
    else:
        try:
            data.remove(sur + " " + name)
            writedata(sorted(data))
        except ValueError:
            print("Данного студента нет в группе")


print("Список команд:\n "
      "add - добавление нового студента в список\n "
      "seek - найти студента по фамилии/фамилии и имени\n "
      "rem - удалить студента из списка\n "
      "ch - изменить информацию о студенте\n "
      "fin - закончить сессию")
while (True):
    s = input("Введите команду: ")
    if (s == "add"):
        surname = input("Введите фамилию студента\n")
        name = input("Введите имя студента\n")
        print(add(surname + " " + name))
    elif (s == "seek"):
        print(seek(input("Введите фамилию студента или фамилию и имя через пробел\n").split()))
    elif (s == "ch"):
        stud = input("Введите фамилию и имя искомого студента через пробел\n")
        new_Surname = input("Введите новую фамилию или '', если вы не хотите менять фамилию\n")
        new_Name = input("Введите новое имя или '', если вы не хотите менять имя\n")
        print(change(stud, new_Surname if (new_Surname != "") else None, new_Name if (new_Name != "") else None))
    elif (s == "rem"):
        surn = input("Введите фамилию студента\n")
        name = input("Введите имя студента или ''\n")
        if (name == ''):
            removal(surn)
        else:
            removal(surn, name = name)
    elif (s == "fin"):
        break
    else:
        print("Команды нет в списке!")
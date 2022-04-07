import json


def add(data):
    (task, categ, time) = (input("Сформулируйте задачу: "), input("Добавьте категорию к задаче: "), input("Добавьте время к задаче: "))
    data.append({"Задача": task, "Категория": categ, "Время": time})
    return data

def getall(data):
    for item in data:
        for key, value in item.items():
            print("{0}: {1}".format(key, value), end="  ")
        print("\n", end="")


flag = True
file_name = input("Введите имя файла формата .json\n")
try:
    file = open(file_name, "r", encoding='utf-8')
    data = json.load(file)
    file.close()
    file = open(file_name, "w")
except:
    print("С этим файлом что-то не так!")
    flag = False
while (flag):
    print("""Простой todo:
            1. Добавить задачу.
            2. Вывести весь список текущих задач.
            3. Выход.""")
    com = input("Введите команду: ")
    if (com == "1"):
        data = add(data)
        print(data)
    elif (com == "2"):
        getall(data)
    elif (com == "3"):
        json.dump(data, file)
        print("Задачи сохранены в файл!")
        file.close()
        flag = False
    else:
        print("Данной команды в списке нет!")
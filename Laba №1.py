documents = [
 {'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'},
 {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
 {'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'}
]

directories = {
 '1': ['2207 876234', '11-2'],
 '2': ['10006'],
 '3': []
}

def search_in_docs(num): #Непосредственный поиск имени владельца по номеру документа
    for i in documents:
        if (i['number'] == num):
            return i
    return None

def search_in_dir(num): #Непосредственный поиск полки по номеру документа
    for i in directories.keys():
        if (num in directories[i]):
            return i
    return None

def check_shelf(num): #Проверка наличия полки
    return num in directories.keys()

def check_absent(num): #Проверка пустоты полки
    return len(directories[num]) == 0

def def_p(num): #Опосредованный поиск имени владельца по номеру документа
    i = search_in_docs(num)
    if (i == None):
        print('Документ не найден в базе')
    else:
        print(f'Владелец документа: {i["name"]}')

def def_s(num): #Опосредованный поиск полки по номеру документа
    i = search_in_dir(num)
    if (i == None):
        print('Документ не найден в базе')
    else:
        print(f'Документ хранится на полке: {i}')

def print_all(): #Печать всех документов в базе documents
    for i in documents:
        num = search_in_dir(i['number'])
        print(f'№: {i["number"]}, тип: {i["type"]}, владелец: {i["name"]}, полка хранения: {num}')
    if (len(documents) == 0):
        print('Документов в базе данных нет')

def add_shelf(num): #Добавление пустой полки
    if (check_shelf(num)):
        print(f'Такая полка уже существует. Текущий перечень полок: {", ".join(list(directories.keys()))}')
    else:
        directories[num] = []
        print(f'Полка добавлена. Текущий перечень полок: {", ".join(list(directories.keys()))}')

def del_shelf(num): #Удаление пустой полки
    if (check_shelf(num)):
        if (check_absent(num)):
            del directories[num]
            print(f'Полка удалена. Текущий перечень полок: {", ".join(list(directories.keys()))}')
        else:
            print(f'На полке есть документы, удалите их перед удалением полки. Текущий перечень полок: {", ".join(list(directories.keys()))}') 
    else:
        print(f'Такой полки не существует. Текущий перечень полок: {", ".join(list(directories.keys()))}')

def add_doc(): #Добавление нового документа в базу данных documents
    new_doc = {}
    new_doc['number'] = input('Введите номер документа: \n')
    new_doc['type'] = input('Введите тип документа: \n')
    new_doc['name'] = input('Введите владельца документа: \n')
    shelf = input('Введите полку для хранения: \n')
    if (check_shelf(shelf)):
        documents.append(new_doc)
        directories[shelf].append(new_doc['number'])
        print(f'Документ добавлен. Текущий список документов:')
        print_all()
    else:
        print('Такой полки не существует. Вы можете добавить новую полку командой ads. \nТекущий список документов:')
        print_all()

def del_doc(num): #Удаление документа из базы данных documents
    i = search_in_docs(num)
    if i == None:
        print('Документ не найден в базе. \nТекущий списко документов:')
        print_all()
    else:
        directories[search_in_dir(num)].remove(num)
        documents.remove(i)
        print('Документ удалён. \nТекщий список документов:')
        print_all()

def move_shelf(): #Перемещение файла из documents на полку из directories
    num = input('Введите номер документа: \n')
    shelf = input('Введите номер полки: \n')
    if (search_in_docs(num) == None):
        print('Документ не найден в базе. \nТекущий список документов:')
    else:
        if (check_shelf(shelf)):
            directories[search_in_dir(num)].remove(num)
            directories[shelf].append(num)
            print('Документ перемещен. \nТекущий список документов:')
            print_all()
        else:
            print(f'Такой полки не существует. Текущий перечень полок: {", ".join(list(directories.keys()))}')

while (True):
    com = input('Введите команду: \n')
    if (com == 'q'):
        break;
    elif (com == 'p'):
        def_p(input("Введите номер документа: "))
    elif (com == 's'):
        def_s(input("Введите номер документа: "))
    elif (com == '|'):
        print_all()
    elif (com == 'ads'):
        add_shelf(input("Введите номер полки: "))
    elif (com == 'ds'):
        del_shelf(input("Введите номер полки: "))
    elif (com == 'ad'):
        add_doc()
    elif (com == 'd'):
        del_doc(input('Введите номер документа: '))
    elif (com == 'm'):
        move_shelf()
    else:
        print('Такой команды нет в списке!')


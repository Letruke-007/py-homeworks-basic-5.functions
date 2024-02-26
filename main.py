documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
      ]

directories = {
        '1': ['2207 876234', '11-2'],
        '2': ['10006'],
        '3': []
      }

# Функция определения ФИО владельца документа
def person(num):
    counter = 0
    for i in range(len(documents)):
        if num == documents[i]['number']:
            print(f'Человек, которому принадлежит документ с номером {num} - {documents[i]['name']}')
            counter += 1
    if counter == 0:
        print('Вы ввели несуществующий номер документа')

# Функция определения номера полки, на которой расположен документ
def shelf_num(num):
    counter = 0
    for key, val in directories.items():
        for i in val:
            if num in i:
                print(f'Документ с номером {num} находится на полке номер {key}')
                counter += 1
    if counter == 0:
        print('Вы ввели несуществующий номер документа')

# Функция вывода в консоль списка всех документов из каталога
def all_docs():
    print('Список документов: ')
    for i in range(len(documents)):
        print(*documents[i].values(), sep=' ')

# Функция добавления нового документа
def add_doc(num, _type, name, _shelf):
    counter = 0
    for key, val in directories.items():
        if _shelf == key:
            counter += 1
            val.append(num)
            new_doc = {'type': _type, 'number': num, 'name': name}
            documents.append(new_doc)
            print('Документ успешно добавлен в каталог и на полку')
    if counter == 0:
        print('К сожалению, такой полки нет архиве, не удалось добавить документ')

# Функция удаления документа
def del_doc(num):
    counter = 0
    for i in range(len(documents)):
        if num == documents[i]['number']:
            counter += 1
            del documents[i]
            print('Удаление документа из каталога завершено успешно.')
            break
    for key, val in list(directories.items()):
        for i in val:
            if num == i:
                counter += 1
                del directories[key]
                print('Удаление документа с полки завершено успешно.')
                break
    if counter == 0:
        print('Ошибка. Вы ввели не существующий документ.')

# Функция перемещение документа с одной полки на другую
def move_doc(num, shelf):
    counter1 = 0
    counter2 = 0
    for key, val in list(directories.items()):
        if num in val:
            counter1 += 1
            r = val.index(num)
            del val[r]
        if shelf == key:
            counter2 += 1
            val.append(num)
            print(f'Документ с номером {num} успешно перемещен на полку номер {shelf}')
    if counter1 == 0:
        print('Документ с таким номером не найден')
    if counter2 == 0:
        print('Полка с таким номером не существует')

# Функция добавления новой полки
def add_shelf(new_shelf_num):
    counter = 0
    for key,val in directories.items():
        if new_shelf_num in key:
            counter += 1
    if counter == 0:
        directories[new_shelf_num] = []
        print('Добавление полки выполнено успешно')
    else:
        print('Полка с указанным Вами номером уже существует')

# Агрегирующая функция - секретарь
def secretary():
    flag = True
    while flag:
        print()
        print('Какую операцию Вы хотите выполнить (введите букву в английском раскладке):')
        print('p - определить ФИО владельца документа')
        print('s - определить номер полки, на которой хранится документ')
        print('l - вывести список всех документов из каталога')
        print('a - добавить новый документ в каталог и на полку')
        print('d - удалить документ из каталога и из полки')
        print('m - переместить существующий документ на другую полку')
        print('as - создать новую полку')
        print('q - завершить работу с каталогом')
        print()
        res = input('')
        if res == 'p':
            num = input('Введите номер документа: ')
            person(num)
        elif res == 's':
            num = input('Введите номер документа: ')
            shelf_num(num)
        elif res == 'l':
            all_docs()
        elif res == 'a':
            num = input('Введите номер документа: ')
            _type = input('Введите тип документа: ')
            name = input('Введите имя владельца документа: ')
            shelf = input('Введите номер полки, на которой будет храниться документ: ')
            add_doc(num, _type, name, shelf)
        elif res == 'd':
            num = input('Введите номер документа: ')
            del_doc(num)
        elif res == 'm':
            num = input('Введите номер документа: ')
            shelf = input('Введите номер полки, на которую нужно переместить документ: ')
            move_doc(num, shelf)
        elif res == 'as':
            new_shelf_num = input('Укажите номер создаваемой полки: ')
            add_shelf(new_shelf_num)
        elif res == 'q':
            break

# Функция функции - секретаря
secretary()

__autor__='Кувалдин Е.А.'
# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py

import shutil, os

def create_dir(dirname):
    dir_path = os.path.join(os.getcwd ())
    try:
        os.mkdir(dir_path + dirname)
    except FileExistEror:
        print('директория с таким именем уже есть')
    return 'Директория создана'

def select_dir (selectDirname):
    dir_path = os.path.join(os.getcwd() + '/' + selectDirname)
    print('Файлы в директории: ', os.listdir(dir_path))

def list_dir():
    print(os.listdir(os.path.join(os.getcwd())))

def whole_menu():
    print('Вы находитесь в директории', os.path.join(os.getcwd()))
    print('Содержание директории : ', list_dir())
    print('Выберите действие из меню: ')
    q = ('1. Перейти в папку', '2. Посмотреть содержимое текущей папки', '3. Удалить папку', '4. Cоздать папку')
    for i in q:
        print(i)
    answer = int(input())
    return answer

def back_menu():
    short_answer = input(str('Вернуться в главное меню ? Y/N'))
    return short_answer
def check_end():
    if back_menu() == 'Y':
        whole_menu()
    else:
        print('До свидания!')


#Начало



while True:
    list_dir()
    answer = whole_menu ()
    if answer == 1:

        myName = str(input('Введите имя папки'))
        select_dir(myName)
        check_end()

    elif answer == 2:
        print('Dir текущей директории: ', list_dir())
        check_end()

    elif answer == 3:
        print('Внимание! Удаление папки!')
        name_for_del = str(input('Введите имя папки для удаления: '))
        try:
           dir_path = os.path.join(os.getcwd() + '\\' + name_for_del)
           os.rmdir(dir_path)
           print('Директория удалена')
        except FileExistsError:
            print('Директория для удаления не найдена')
        check_end()
    elif answer == 4:
        print('Внимание! Сщздание новой директории!')
        name_new_dir = str(input('Введите имя для новой папки: '))
        dir_path = os.path.join ( os.getcwd () + '/' + name_new_dir)
        try:
            os.mkdir(dir_path)
            print('Новая папка зоздана: ', name_new_dir)
        except FileExistError:
            print('Такая директория уже существует')
        check_end()















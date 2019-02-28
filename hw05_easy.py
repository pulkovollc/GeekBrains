__autor__= 'Кувалдин Е. А.'
# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
import os

print('Созданы директории:')
for i in range(1, 9):
    dir_path = os.path.join(os.getcwd(), 'dir_' + str(i))
    print(dir_path)
    try:
        os.mkdir(dir_path)
    except FileExistsError:
        print('Такая директория уже существует')

myAnswer = input('Удалять созданные директории? Y/N')
if myAnswer == 'N':
    print('До свидания!')
elif myAnswer == 'Y':
    myItemFrom = os.listdir()
    for i in myItemFrom:
        if 'dir_' in i:
            os.rmdir(os.getcwd() + '/' + str(i))
print('Сделано')

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
print('Созданы директории:')
for i in range(1, 9):
    dir_path = os.path.join(os.getcwd(), 'dir_' + str(i))
    print(dir_path)
    try:
        os.mkdir(dir_path)
    except FileExistsError:
        print('Такая директория уже существует')
myItemFrom2 = os.listdir()
for i in myItemFrom2:
    if os.path.isdir(os.getcwd() + '/' + i) == True:
        print(i, '-директория')
    else:
        pass

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.


import shutil
print('Запущен скрипт из этого файла: ', os.path.basename(__file__))
myFile = os.getcwd() + '/' + os.path.basename(__file__)
myNewFile = os.getcwd() + '/' + os.path.basename(__file__) + '.copy'
try:
    copyfile(myFile, myNewFile)
except FileExistsError:
    print('копия уже создана')
print('Копия создана')


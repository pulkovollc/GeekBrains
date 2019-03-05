__autor__='Кувалдин Е.А.'

# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать 
# в неограниченном кол-ве классов свой определенный предмет. 
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика 
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе
class School():

    def __init__(self, classes, teachers, metters):
        self.classes = classes
        self.teachers = teachers
        self.metters = metters

    def ad_classes():
        return list(map(str, input('Введите наименование классов').split()))

    def ad_teachers():
        return list(map(str, input('Введите фамилии учителей').split()))

    def ad_metters():
        return list(map(str, input('Какие предметы есть в школе?').split()))

    def ad_studients():
        return list(map(str, input('Какие фамилии у учеников?').split()))

    def ad_patents():
        return list(map(str, input('Какие фамилии у родителей?').split()))
class Dict_maker():
    def __init__(self, one_volume, second_volume):
        self.one_volume = one_volume
        self.second_volume = second_volume

    def ad(self):
        scd = {}
        met = []
        for i in self.one_volume:
            for n in self.second_volume:
                print(i, 'добавлять в {}?'.format(n))
                l = str(input('Y/N?'))
                if l == 'Y':
                    met.append(n)
                else:
                    pass
            scd.update({i: met})
            met = []

        return scd

def exit()
    print('До свидания!')

# Заполняем словари
# Предметы
print('Заполниете премдметы в школе, через пробелы в строку')
my_mett = School.ad_metters()

# Фамилии учителей
print('Фамилии учителей')
my_teach = School.ad_teachers()

# Школьные классы
print('Школьные классы')
my_classes = School.ad_classes()

# Фамилии учеников
print('Фамилии учеников')
my_studients = School.ad_studients()

# Фамилии родителей
print('Фамилии родителей')
my_parents = School.ad_patents()

# Создаем словарь учитель\предметы
print('Распределите учителей по предметам')
my_tech_metter = Dict_maker(my_mett, my_teach).ad()

# Создаем словарь студенты\классы
print('Распределите учеников по классам')
my_stud_classes = Dict_maker(my_studients, my_classes).ad()

# Создаем словарь родители\студенты
print('Распределите родителей по ученикам')
my_parents_stud = Dict_maker(my_parents, my_studients).ad()

# Создаем словарь родители\студенты
print('Распределите учителей по классам')
my_teach_classes = Dict_maker(my_teach, my_classes).ad()

class Menu():

    def start():

        print('Выбирайте нужный раздел:')

        my_menu = ['1.Родители/ ученики', '2.Предметы/ учители', '3.Учители/ классы', '4.Ученики/ классы']
        for i in my_menu:
            print(i)


    def my_answer():

        answer = int(input('Введите номер меню:'))

        if answer == 1:
            print('Родители - ученики')
            print()

            for i in my_parents_stud.keys():
                for n in my_parents_stud.get(i):
                    print(i, '-', n)
            print()
            Back_Menu()

        elif answer == 2:
            print('Предмет - учитель')
            print()
            for i in my_tech_metter.keys():
                for n in my_tech_metter.get(i):
                    print(i, '-', n)
            print()
            Back_Menu()

        elif answer == 3:
            print('Учитель - Класс')
            print()
            for i in my_teach_classes.keys():
                for n in my_teach_classes.get(i):
                    print(i,'-',n)
            print()
            Back_Menu()


        elif answer == 4:
            print('Ученик - класс')
            print()
            for i in my_stud_classes.keys():
                for n in my_stud_classes.get(i):
                    print(i,'-',n)
            print()
            Back_Menu()

def exit():
    print('До свидания!')
def Back_Menu():

    answer = input(str('Вернуться в главное меню? Y/N'))
    if answer == 'Y':
        Menu.start()
    else:
        print('До свидания!')

## Начало
Menu.start()
while True:
    Menu.my_answer()
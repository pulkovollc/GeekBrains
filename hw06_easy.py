__autor__="Кувалдин Е.А."
# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

# Создание родительсткого класса хранящего координаты фигур разного типа
from math import sqrt
class figure():

    def __init__(self, cordinates):
        self.cordinates = cordinates

# Дочерний класс треугольник, унаследовавший описание координат из родительсткого класса 'figure'
class tringle(figure):

    def __init__(self, cordinates):
        self.cordinates = cordinates


    def square(self):

        return abs(self.cordinates[0]*(self.cordinates[3] - self.cordinates[5]) + self.cordinates[2]*(self.cordinates[5] - self.cordinates[1]) + self.cordinates[4]*(self.cordinates[1] - self.cordinates[3]))/ 2.0

    def perim(self):

        return sqrt((self.cordinates[0]-self.cordinates[2])*(self.cordinates[0]-self.cordinates[2]) + (self.cordinates[1]-self.cordinates[3])*(self.cordinates[1]-self.cordinates[3])) + sqrt((self.cordinates[0]-self.cordinates[4])*(self.cordinates[0]-self.cordinates[4]) + (self.cordinates[1]-self.cordinates[5])*(self.cordinates[1]-self.cordinates[5])) + sqrt((self.cordinates[2]-self.cordinates[4])*(self.cordinates[2]-self.cordinates[4]) + (self.cordinates[3]-self.cordinates[5])*(self.cordinates[3]-self.cordinates[5]))


print('Введите последовательно координаты треугольника без запятой: x1, y1, x2, y2, x3, y3')


# Последовательный ввод координат треугольника с строку
sq_tr = list(map(int, input().split()))

# Расчет площади треуголька и вывод результата
p = tringle(sq_tr).square()
print('Площадь треугольника = {} кв. ед.'.format(p))

# Расчет периметра треугольника и вывод результата
trin_per = tringle(sq_tr).perim()
print('Периметр треугольника = {} ед.'.format(trin_per))

print('Задача №2')
# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

class trapezium(figure):

    def __init__(self, cordinates):
        self.cordinates = cordinates

    def sq_tr(self):

       return ((self.cordinates[6] - self.cordinates[0])/2 * (self.cordinates[3]-self.cordinates[1]))

    def check(self):

        if (self.cordinates[2] - self.cordinates[0]) == (self.cordinates[6] - self.cordinates[4]):
            return True
        else:
            return False

    def trap_perim(self):

        self.sidel = []
        self.sidel.append(sqrt(((self.cordinates[2] - self.cordinates[0])**2) + (self.cordinates[3] - self.cordinates[1])**2))

        self.sidel.append(sqrt(((self.cordinates[4] - self.cordinates[2]) ** 2) + (self.cordinates[5] - self.cordinates[3]) ** 2))

        self.sidel.append(sqrt(((self.cordinates[6] - self.cordinates[4]) ** 2) + (self.cordinates[7] - self.cordinates[5]) ** 2))

        self.sidel.append(sqrt(((self.cordinates[0] - self.cordinates[6]) ** 2) + (self.cordinates[1] - self.cordinates[7]) ** 2))

        return self.sidel

# Ввод координаттрапеции
print('Введите координаты вершин трапеции, нижнее осевание (x1:x4)')
tr_cr = list(map(int, input().split()))

# Вывод результатов
print('Площадь трапеции = {} кв. ед'.format(trapezium(tr_cr).sq_tr()))
print('Утверждение, что эта трапеция равнобокая - {}'.format(trapezium(tr_cr).check()))
print('Длины сторон трапеции:')
n = 0
for i in trapezium(tr_cr).trap_perim():
    n += 1
    print('Сторона {} имеет длину {} ед.'.format(n, i))
print('Периметр трапеции: {}, ед.'.format(sum(trapezium(tr_cr).trap_perim())))

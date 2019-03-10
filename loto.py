__autor_ = 'Кувалдин Е.А.'

"""
== Лото ==

Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа, 
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр, 
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86 
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается 
случайная карточка. 

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.

Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71   
--------------------------
-- Карточка компьютера ---
 7 11     - 14    87      
      16 49    55 77    88    
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать 
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать 
модуль random: http://docs.python.org/3/library/random.html

"""
import random
import copy

"""""
Создаем один класс, с большим количеством методов

"""
class Card:
    def __init__(self, lottery):
        self.rownum = 3
        self.colnum = 9
        self.lottery = lottery

    def add(self, n = 9):
        self.n = n

        while self.n > 0:
            self.num = random.randint(1, 90)
            if self.num in self.lottery:
                pass
            else:
                self.lottery.append(self.num)
                self.n -= 1
                self.lottery.sort()
        self.p = 4
        self.emty_side =[]
        while self.p > 0:
            self.empty_rand=random.randint(0, 8)
            if self.empty_rand in self.emty_side:
                pass
            else:
                self.lottery.pop(self.empty_rand)
                self.lottery.insert(self.empty_rand, '')
                self.emty_side.append(self.empty_rand)
                self.p -= 1
        return self.lottery

    def cube_generator(self):
        self.rand_nums = 90
        self.random_list = []

        while self.rand_nums > 0:
            self.random_cube = random.randint(1, 90)
            if self.random_cube in self.random_list:
                pass
            else:
                self.random_list.append(self.random_cube)
                self.rand_nums -= 1
        return self.random_list

    def ready_lottery(self):
        self.readyLottery = []
        for i in range(3):
            self.readyLottery.append(Card([]).add())
        return self.readyLottery

    def next_cube(self, iter_list):
        self.iter_list = iter_list
        return next(self.iter_list)

    def check_lottery(self, lottery, num):
        self.n = 3
        self.pos = 0
        self.num = num
        self.lottery = lottery
        self.count_position = 0
        self.segment = 0
        for i in self.lottery:
            if self.num in i:
                self.pos = i.index(self.num)
                self.count_position += 1
                self.segment = self.count_position

            else:
                self.n -= 1
                self.count_position += 1
        if self.n == 0:
            return 'Такого числа нет! Вы проиграли!'
        else:
            self.lottery[self.segment - 1].pop(self.pos)
            self.lottery[self.segment - 1].insert(self.pos, '-')

        return self.lottery


def check_int(lottery):
    count = 0
    for i in lottery:
        for n in i:
            if type(n) == int:
                count += 1
            else:
                pass
    return count

def my_print(lottery):

    for i in lottery:
        for n in i:
            if type(n)==int:
                spell = n
            elif n =='-':
                spell = '-'
            else:
                spell = '\x20 '
            print(str(spell)+'\x20', sep='\x20 ', end='')

        print('')

# Создаем последовательнсоть выброшенных ходов от 1 до 90 с помошью метода 'cube_generator()' в классе 'Card'
random_cube_line = Card([]).cube_generator()
random_cube_line = iter(random_cube_line)

# Создаем карты игровые для игрокаи компьютера пр ипомощи функции
player_card = Card([]).ready_lottery()
computer_card = Card([]).ready_lottery()

print()
print('-------Карта игрока---------')
my_print(player_card)
print()
print('-------Карта компьютера-----')
my_print(computer_card)
input('Карты выпали такие! Для продолжения игры нажмите любую кнопку')
s = 90

row_cube =[]
while s > 0:
    raNum = next(random_cube_line)
    row_cube.append(raNum)
    Card([]).check_lottery(player_card, raNum)
    Card([]).check_lottery(computer_card, raNum)
    pc = check_int(player_card)
    cc = check_int(computer_card)
    if pc == 0 or cc == 0:
        break
    else:
        pass
    s -= 1

if pc < cc:
    end='Победили вы!!!!'
else:
    end ='Увы, удача на стороне компьютера.'

print()
print('-------Карта игрока---------')
my_print(player_card)
print()
print('-------Карта компьютера-----')
my_print(computer_card)
print()
print('Боченки {} шт. выпадали в это порядке:'.format(len(row_cube)))
print(row_cube)
print(end)



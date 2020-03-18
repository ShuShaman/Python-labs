from random import shuffle, random  # смешивание комада
import itertools
import time
from time import strftime
from datetime import timedelta, datetime


# Написать декоратор non_empty, проверяющий списковый результат любой функции:
# если в нем содержатся пустые строки или значение None, то они удаляются


def non_empty(func):
    def wrapper():
        returned = func()
        deleted = 0

        for i in returned:
            if i is None or i == '':
                returned.pop(deleted)
            deleted += 1
        return returned
    return wrapper


@non_empty
def get_pages():
    return ['chapter1', '', 'contents', '', 'line1']


def task14():
    print(get_pages())


# task14()


#  Напишите параметризированный декоратор pre_process, который
# осуществляет предварительную обработку (цифровую фильтрацию)
# списка по алгоритму: s[i] = s[i]–a∙s[i–1]. Параметр а можно задать в
# коде (по умолчанию равен 0.97). Пример кода:

# @pre_process(a=0.93)
# def plot_signal(s):
# for sample in s:
# print(sample)

def pre_process(a=0.97):
    def decorator(func):
        def wrap(*args):  # внутри args содержится 0 или более элементов с данными
            s = args[0]
            for i in range(1, len(s)):
                s[i] = s[i] - a * s[i - 1]
            print('a = ', a)
            func(s)

        return wrap

    return decorator


@pre_process(a=0.95)
def plot_signal(s):
    for sample in s:
        print(sample)


def task15():
    arr = [i for i in range(10)]
    plot_signal(arr)


# task15()


# Напишите скрипт, который на основе списка из 16 названий
# футбольных команд случайным образом формирует 4 группы по 4
# команды, а также выводит на консоль календарь всех игр (игры
# должны проходить по средам, раз в 2 недели, начиная с 14 сентября
# текущего года). Даты игр необходимо выводить в формате «14/09/2016,
# 22:45». Используйте модуль random.


def task16():
    format = "%d/%m/%Y, %H:%M"
    start = datetime.strptime("14/09/2016, 22:45", format)
    teams = [
        '1', '2', '3', '4',
        '5', '6', '7', '8',
        '9', '10', '11', '12',
        '13', '14', '15', '16'
    ]
    shuffle(teams)  # смешивание команд
    teams = [teams[i * 4: i * 4 + 4] for i in range(0, 4)]
    games = []
    for t in teams:
        games.append([c for c in itertools.combinations(t, 2)])
    [print('Group ', i+1, ' - ', teams[i]) for i in range(len(teams))]
    for i in range(0, 6):
        print(start.strftime(format))
        print("Game: ", i + 1)
        print(games[0][i])
        print(games[1][i])
        print(games[2][i])
        print(games[3][i])
        start = start + timedelta(days=14)

    print(start.strftime(format))

task16()


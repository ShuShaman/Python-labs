import re
import random
import math


# Напишите  программу,  позволяющую  ввести  с  клавиатуры  текст предложения и
# вывести на консоль все символы, которые входят в этот текст ровно по одному разу.


def task6():
    text = list(input('Введите текст предложения\n'))
    print('Уникальные символы:\n', ' '.join([i for i in text if text.count(i) == 1]))



task6()


# Напишите скрипт,  который обрабатывает  список  строк-адресов следующим образом:
# сначала определяет, начинается ли каждая строка в  списке с префикса «www».  Если условие
# выполняется,  то скрипт должен вставить в  начало  этой строки  префикс «http://»,
# а затем проверить, что строка заканчивается на «.com». Если у строки другое окончание,
# то скрипт  должен вставить  в  конец  подстроку«.com».В итоге скрипт должен вывести на
# консоль новый список с измененными адресами.Используйте генераторы списков


def task7():
    sites = ["www.metanit.com", "proglib.com", "www.stepik.org", "www.google", "github.com"]
    print(" ".join([i + ".com" if (".com" not in i) else i for i in ["http://" + i for i in sites if ("www." in i)]]))


# task7()


# Напишите  скрипт, генерирующий случайным  образом  число n в диапазоне от  1  до  10000.
# Скрипт  должен  создать  массив  из n целых чисел,  также  сгенерированных  случайным  образом,
# и дополнить массив нулями до размера, равного ближайшей сверху степени двойки. Например,
# если  в  массиве  было n=100  элементов,  то  массив нужно дополнить 28 нулями,
# чтобы в итоге был массив из 28=128 элементов (ближайшая степень двойки к 100 –это число 128,
# к35 –это 64 и т.д.).


def task8():
    array = [random.randint(0, 100) for i in range(0, random.randint(0, 10000))]
    print("Первоначальное число элементов", len(array))
    for i in range(len(array), 2**math.ceil(math.log2(len(array)))):
        array.append(0)
    print("Число элементов сейчас", len(array))

task8()


# Напишите  программу,имитирующую  работу  банкомата.Выберите структуру данных для
# хранения купюр разного достоинствав заданном количестве.При  вводе  пользователем
# запрашиваемой суммы  денег, скрипт  должен вывести  на  консоль  количество  купюр
# подходящего достоинства. Если  имеющихся  денег  не  хватает,  то необходимо напечатать сообщение
# «Операция  не  может  быть выполнена!».Например, при сумме 5370 рублей на консоль должно
# быть выведено «5*1000 + 3*100 + 1*50 + 2*10».'''


def task9():
    money = {1000: 1, 500: 10, 100: 10, 50: 10, 10: 1}
    user = int(input("Введите сумму: "))
    if money[1000] * 1000 + money[500] * 500 + money[100] * 100 + money[50] * 50 + money[10] * 10 < user:
        print("Операция не может быть выполнена!")
        return 0
    money1 = str([(mul, i) for i, mul in task9_generator(money, user)])
    print(money1.replace("[(", '').replace(")]", "").replace("), (", " + ").replace(",", " *"))


def task9_generator(bank, user):
    for i in bank:
        tmp = (user / i) // 1 if (user / i) // 1 <= bank[i] else bank[i]
        user -= tmp * i
        yield int(tmp), i


 # task9()


# Напишите  скрипт,  позволяющий  определить  надежность  вводимого
# пользователем  пароля.Это  задание  является  творческим: алгоритм
# определения надежности разработайте самостоятельно.


def task10():
    max_len = 25
    passw = input('Введите пароль (не больше 25 символов): ')

    if len(passw) < 1 or len(passw) > max_len:
        raise Exception('ERROR! Incorrect length of password!')

    same_characters = False
    abc = "abcdefghijklmnopqrstuvwxyzабвгдеёжзийклмнопрстуфхцчшщъыьэюя.,:;!_*-+()/#^%&0123456789"
    for i in abc:
        if passw == i * len(passw.lower()):
            same_characters = True

    symbols = any(char in ".,:;!_*-+()/#^%&)" for char in passw)

    very_weak = same_characters
    weak = passw.isalpha() or passw.islower() or passw.isupper() or passw.isnumeric() or len(passw) < 8
    normal = not passw.isalpha() and not passw.islower() and len(passw) < 12
    good = not passw.isalpha() and not passw.islower()
    strong = symbols and not passw.isalpha() and not passw.islower() and not passw.isnumeric()

    if very_weak:
        print('Очень слабый пароль. Состоит из одинаковых символов')
    elif weak:
        print('Слабый пароль')
    elif normal:
        print('Средний пароль')
    elif good:
        print('Хороший пароль')
    elif strong:
        print('Надежный пароль')


#task10()
# Напишите генератор frange как аналог range() с дробным шагом.
# Пример вызова:
#
# for x in frange(1, 5, 0.1):
# print(x)
# # выводит 1 1.1 1.2 1.3 1.4 … 4.9 5.0


def frange(first, last, step):
    while first <= last:
        yield round(first, 1)  # округление до десятых
        first += step


def task11():
    for x in frange(1, 5, 0.5):
        print(x, end="  ")


# task11()

# Напишите генератор get_frames(), который производит «оконную
# декомпозицию» сигнала: на основе входного списка генерирует набор
# списков – перекрывающихся отдельных фрагментов сигнала размера
# size со степенью перекрытия overlap. Пример вызова:
# for frame in get_frames(signal, size=1024, overlap=0.5):
# print(frame)


def get_frames(signal, size, overlaps):
    step = int(size * overlaps)
    start = 0
    while start < len(signal) - 1:
        yield signal[start: start + size]
        start += step


def task12():
    signal = [i for i in range(10)]
    print(signal)
    print('\n')
    for frame in get_frames(signal, 4, 0.5):
        print(frame)


# task12()

# Перекрытие - это значение, на которое следующий лист будет заходить на пределы предыдущего(с округлением)


# Напишите собственную версию генератора enumerate под названием
# extra_enumerate. Пример вызова:
# for i, elem, cum, frac in extra_enumerate(x):
#  print(elem, cum, frac)
#
# В переменной cum хранится накопленная сумма на момент текущей
# итерации, в переменной frac – доля накопленной суммы от общей
# суммы на момент текущей итерации. Например, для списка x=[1,3,4,2]
# вывод будет таким:
#  (1, 1, 0.1)   (3, 4, 0.4)     (4, 8, 0.8)     (2, 10, 1)


def extra_enumerate(x):
    a_sum = 0
    fraction = 0
    for step in x:
        fraction += step
    for i in range(len(x)):
        a_elem = x[i]
        a_sum += x[i]
        frac = a_sum / fraction
        yield i, a_elem, a_sum, round(frac, 1)


def task13():
    x = [x for x in range(15)]
    for i, a_elem, a_sum, frac in extra_enumerate(x):
        print(a_elem, a_sum, frac)


# task13()


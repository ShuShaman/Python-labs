# Напишите простой класс StringFormatter для форматирования строк со
# следующим функционалом:
# – удаление всех слов из строки, длина которых меньше n букв;
# – замена всех цифр в строке на знак «*»;
# – вставка по одному пробелу между всеми символами в строке;
# – сортировка слов по размеру;
# – сортировка слов в лексикографическом порядке.
# Примечание. Разделители слов можно задавать отдельно. По
# умолчанию в качестве разделителя принимается только символ
# пробела


class StringFormatter:
    def delNLines(self, string, n):
        wordslist = string.split(' ')
        for i in wordslist:
            if len(i) < n:
                wordslist.remove(i)
        return ' '.join(wordslist)

    def replaceNumbers(self, string):
        tempstr = string.translate(str.maketrans('0123456789', '**********'))
        return tempstr

    def addSpaces(self, string):
        tempstr = ''
        for i in string:
            if not i == ' ':
                tempstr += i + ' '
        return tempstr

    def sortByLenght(self, string):
        def SBL(str):
            return len(str)

        templst = string.split(' ')
        templst.sort(key=SBL)
        return ' '.join(templst)

    def lexOrder(self, string):
        lexlist = string.split(' ')
        leslist = sorted(lexlist, key=lambda x: (str.lower(x), x))
        return ' '.join(lexlist)


SFor = StringFormatter()

print(SFor.delNLines('12 123456 1234 1234567 12345', 3))
print(SFor.replaceNumbers('4 лабы и 8 индивидуальных'))
print(SFor.addSpaces('Программирование'))
print(SFor.sortByLenght('Сортировка слов по размеру почему бы и нет'))
print(SFor.lexOrder('Сортировка слов по лексическому значению'))
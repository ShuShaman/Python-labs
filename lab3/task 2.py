# Напишите классы «Книга» (с обязательными полями: название, автор,
# код), «Библиотека» (с обязательными полями: адрес, номер) и
# корректно свяжите их. Код книги должен назначаться автоматически
# при добавлении книги в библиотеку (используйте для этого
# статический член класса). Если в конструкторе книги указывается в
# параметре пустое название, необходимо сгенерировать исключение
# (например, ValueError). Книга должна реализовывать интерфейс
# Taggable с методом tag(), который создает на основе строки набор тегов
# (разбивает строку на слова и возвращает только те, которые
# начинаются с большой буквы). Например, tag() для книги с названием
# ‘War and Peace’ вернет список тегов [‘War’, ‘Peace’]. Реализуйте классы
# таким образом, чтобы корректно выполнялся следующий код:
# lib = Library(1, ’51 Some str., NY’)
# lib += Book(‘Leo Tolstoi’, ‘War and Peace’)
# lib += Book(‘Charles Dickens’, ‘David Copperfield’)
# for book in lib:
# # вывод в виде: [1] L.Tolstoi ‘War and Peace’
# print(book)
# # вывод в виде: [‘War’, ‘Peace’]
# print(book.tag())


class Taggable(object):
    def tag(self):
        raise NotImplementedError("Не реализован метод tag у Book")


class Book(Taggable):
    key = 1

    def __init__(self, name, author):
        assert (len(name) != 0), "Введите название книги!"
        assert (len(author) != 0), "Введите автора книги!"
        self.name = name
        self.author = author
        self.key = self.__class__.key
        self.__class__.key += 1

    def tag(self):
        res = self.name.split()
        for x in res:
            if not x.istitle():
                res.remove(x)
                return res

    def __str__(self):
        aut = self.author.split(' ')
        LastName = aut[1:]
        LastName = str(LastName)
        return '[%d] %.1s. %s "%s"' % (self.key, self.author, LastName, self.name)


class Library(Book):
    def __init__(self, number, name):
        assert (len(name) != 0), "Введите название библиотеки!"
        self.number = number
        self.name = name
        self.book = []
        self.itr = -1

    def __iadd__(self, other):
        self.book.append(other)
        return self

    def itr(self):
        return self.book

    def __iter__(self):
        return self

    def __next__(self):
        self.itr = self.itr + 1
        if self.itr < len(self.book):
            name = self.book[self.itr].name
            author = self.book[self.itr].author
            key = self.book[self.itr].key
            # print('[' + str(key) + '] ' + author + ' \'' + name + '\'')
            return self.book[self.itr]
        raise StopIteration


lib = Library(1, '51 Some str., NY')
lib += Book('War and Peace', 'Lev Tolstoi')
lib += Book('Игра престолов', 'Джордж Р. Р. Мартин')

for book in lib:
    print(book)
    print(book.tag())

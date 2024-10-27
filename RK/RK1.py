from operator import itemgetter

class Library:
    """Библиотека"""
    def __init__(self, id, name):
        self.id = id
        self.name = name

class ProgrammingLanguage:
    """Язык программирования"""
    def __init__(self, id, name, popularity, library_id):
        self.id = id
        self.name = name
        self.popularity = popularity
        self.library_id = library_id

class LibraryLanguage:
    """Связь между библиотеками и языками программирования (многие ко многим)"""
    def __init__(self, library_id, language_id):
        self.library_id = library_id
        self.language_id = language_id

# Библиотеки
libraries = [
    Library(1, "Библиотека алгоритмов"),
    Library(2, "Библиотека анализа данных"),
    Library(3, "Библиотека веб разработки"),
    Library(4, "Библиотека мобильной разработки"),
    Library(5, "Библиотека машинного обучения"),
    Library(6, "Библиотека сетевой безопасности"),
]

# Языки программирования
languages = [
    ProgrammingLanguage(1, "Python", 10, 1),
    ProgrammingLanguage(2, "JavaScript", 8, 2),
    ProgrammingLanguage(3, "Java", 7, 3),
    ProgrammingLanguage(4, "C++", 6, 3),
    ProgrammingLanguage(5, "R", 5, 3),
]

# Связи библиотек и языков программирования
library_languages = [
    LibraryLanguage(1, 1),
    LibraryLanguage(2, 2),
    LibraryLanguage(3, 3),
    LibraryLanguage(3, 4),
    LibraryLanguage(3, 5),
    LibraryLanguage(4, 1),
    LibraryLanguage(5, 2),
    LibraryLanguage(6, 3),
    LibraryLanguage(6, 4),
    LibraryLanguage(6, 5),
]

def main():
    one_to_many = [(l.name, l.popularity, lib.name)
                   for lib in libraries
                   for l in languages
                   if l.library_id == lib.id]

    many_to_many_temp = [(lib.name, l.library_id, l.language_id)
                         for lib in libraries
                         for l in library_languages
                         if lib.id == l.library_id]

    many_to_many = [(lang.name, lang.popularity, library_name)
                    for library_name, library_id, language_id in many_to_many_temp
                    for lang in languages if lang.id == language_id]

    # Сортировка по библиотекам
    print('Задание A1')
    res_1 = sorted(one_to_many, key=itemgetter(2))
    print(res_1)

    # Сортировка библиотек по суммарной популярности языков
    print('\nЗадание A2')
    res_2 = []
    for lib in libraries:
        temp_lib = list(filter(lambda i: i[2] == lib.name, one_to_many))
        total_popularity = 0
        if len(temp_lib) > 0:
            for i in temp_lib:
                total_popularity += i[1]
            res_2.append((lib.name, total_popularity))

    res_2 = sorted(res_2, key=itemgetter(1))
    print(res_2)

    # Список всех библиотек, в названии которых есть слово "разработки" с языками программирования в них
    print('\nЗадание A3')
    res_3 = {}
    for lib in libraries:
        if 'разработки' in lib.name:
            this_lib = list(filter(lambda i: i[2] == lib.name, many_to_many))
            lang_list = [i[0] for i in this_lib]
            res_3[lib.name] = lang_list

    print(res_3)

if __name__ == '__main__':
    main()
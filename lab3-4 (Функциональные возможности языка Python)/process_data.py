import json
from print_result import print_result
from cm_timer import cm_timer_1
from gen_random import gen_random
from unique import Unique

path = 'data_light.json'

with open(path) as f:
    data = json.load(f)

@print_result
def f1(arg):
    return sorted(Unique([job['job-name'].lower() for job in arg if 'job-name' in job]), key=lambda x: x.lower())
    #извлекает значения по ключу 'job-name', приводит их к нижнему регистру, удаляет дубликаты и сортирует в алфавитном порядке.

@print_result
def f2(arg):
    # Фильтрация профессий, которые начинаются со слова "программист"
    return list(filter(lambda x: x.startswith('программист'), arg))

@print_result
def f3(arg):
    # Добавление строки "с опытом Python" к каждой профессии
    return list(map(lambda x: f"{x} с опытом Python", arg))

@print_result
def f4(arg):
    # Генерация зарплаты и объединение с названием профессии
    salaries = gen_random(len(arg), 100000, 200000)
    return list(map(lambda x, y: f"{x}, зарплата {y} руб.", arg, salaries))

if __name__ == '__main__':
    with cm_timer_1():
        f4(f3(f2(f1(data))))

#
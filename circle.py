import math
'''Импорт библиотеки math для работы с числом pi'''

def area(r):
    '''Принимает радиус окружности, возвращает площадь окружности'''
    if str(r).isalpha() == 1:
        return TypeError
    if r <= 0:
        return ValueError
    return (math.pi * r * r)
    

def perimetr(r):
    '''Функция получает радиус, вычисляет периметр окружности'''
    if str(r).isalpha() == 1:
        return TypeError
    if r <= 0:
        return ValueError
    return 2 * math.pi * r


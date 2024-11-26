import math
'''Импорт библиотеки math для работы с числом pi'''

def area(r):
    '''Принимает радиус окружности, возвращает площадь окружности'''
    if not isinstance(r, (int, float)):
        raise TypeError("Радиус должен быть числом")
    if r <= 0:
        raise ValueError("Радиус должен быть положительным")
    return math.pi * r * r

def perimetr(r):
    '''Функция получает радиус, вычисляет периметр окружности'''
    if not isinstance(r, (int, float)):
        raise TypeError("Радиус должен быть числом")
    if r <= 0:
        raise ValueError("Радиус должен быть положительным")
    return 2 * math.pi * r


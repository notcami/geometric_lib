def area(a, h): 
    if str(a).isalpha() == 1 or str(h).isalpha() == 1:
        return TypeError
    if a <= 0 or h <= 0:
        return ValueError
    return a * h / 2 

    '''Программа получает a и h - сторона и высота треугольника, возвращает a*h / 2 (площадь треугольника)'''

def perimetr(a, b, c): 
    if str(a).isalpha() == 1 or str(b).isalpha() == 1 or str(c).isalpha() == 1:
        return TypeError
    if a <= 0 or b <= 0 or c <= 0:
        return ValueError
    return a + b + c 

    '''Программа получает три числа: a, b, c - стороны треугольника, возвращает их сумму (периметр)'''

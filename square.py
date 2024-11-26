def area(a):
    if str(a).isalpha() == 1:
        return TypeError
    if a <= 0:
        return ValueError
    return a * a

    '''Программа получает число a , возвращает a * a (площадь квадрата)''' 

def perimetr(a):
    if str(a).isalpha() == 1:
        return TypeError
    if a <= 0:
        return ValueError
    return 4 * a

    '''Программа получает число a , возвращает a*4 (периметр квадрата)'''

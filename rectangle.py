def area(a, b):
    '''
    Программа получает на вход два числа: a и b, а возвращает их произведение (площадь)
    '''
    if str(a).isalpha() == 1 or str(b).isalpha() == 1:
        return TypeError
    if a <= 0 or b <= 0:
        return ValueError
    return a * b
        

def perimetr(a, b): 
    '''Функция получает два числа: а и b , возвращает их сумму, умноженную на 2 (периметр)'''
    if str(a).isalpha() == 1 or str(b).isalpha() == 1:
        return TypeError
    if a <= 0 or b <= 0:
        return ValueError
    return 2 * (a + b)
print(perimetr(3, 4))

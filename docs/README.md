Solution:
Added functions for calculating the area and perimeter of shapes: circle, rectangle, square, triangle
Description of functions:
Circle:
import math

def area(r):
return math.pi * r * r

def perimetr(r):
return 2 * math.pi * r
Importing the math library for working with pi
import math
The function for calculating the area takes the number r - the radius of the circle for further calculation of the area of ​​the circle
def area(r):
Returns the area of a circle
return math.pi * r * r
The function for calculating the perimeter of a circle takes the number r - the radius of the circle to calculate the perimeter of the circle
def perimetr(r):
The program returns the perimeter of the circle
return 2 * math.pi * r
Example call:
import math

def area(r):
    return math.pi * r * r

def perimetr(r):
    return 2 * math.pi * r

int r = 5
print(area(r))
print(perimetr(r))
Rectangle
def area(a, b):
    return a * b

def perimetr(a, b):
    return 2 * (a + b)
Takes two numbers: a and b - the length and width of the rectangle to calculate its area
def area(a, b):
Returns the area of a rectangle
return a * b
The function for calculating the perimeter takes two numbers: a and b - the length and width of the rectangle to calculate its perimeter
def perimetr(a, b):
Returns the perimeter of a rectangle
return 2 * (a + b)
Example call:
def area(a, b):
    return a * b

def perimetr(a, b):
    return 2 * (a + b)

int a = 5
int b = 6
print(area(a, b))
print(perimetr(a, b))
Square
def area(a):
    return a * a

def perimetr(a):
    return 4 * a
The function for calculating the area takes the number a - the side of the square to calculate its area
def area(a):
Returns the area of a square
return a * a
The function for calculating the perimeter takes the number a - the side of the square to calculate its perimeter
def perimetr(a):
Returns the perimetr of a square
return 4 * a
Example call:
def area(a):
    return a * a

def perimetr(a):
    return 4 * a

int a = 10
print(area(a))
print(perimetr(a))
Triangle
def area(a, h):
    return a * h / 2

def perimetr(a, b, c):
    return a + b + c
The function for calculating the area takes two numbers: a and h - the side and height of the triangle to calculate its area
def area(a, h):
Returns the area of a triangle
return a * h / 2
The function for calculating the perimeter takes three numbers: a, b, c - sides of the triangle
def perimetr(a, b, c):
Returns the perimetr of a triangle
return a + b + c
Example call:
def area(a, h):
    return a * h / 2

def perimetr(a, b, c):
    return a + b + c

int a = 5
int b = 4
int c = 3
int h = 2
print(area(a, h))
print(perimetr(a, b, c))

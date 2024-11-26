# Solution:
## Added functions for calculating the area and perimeter of shapes: circle, rectangle, square, triangle

# Description of functions:
## Circle:
```python
import math

def area(r):
return math.pi * r * r

def perimetr(r):
return 2 * math.pi * r
```
- Importing the math library for working with pi

```python
import math
```
- The function for calculating the area takes the number **r** - the radius of the circle for further calculation of the area of ​​the circle

```python
def area(r):
```
- Returns the area of a circle


```python
return math.pi * r * r
```
- The function for calculating the perimeter of a circle takes the number **r** - the radius of the circle to calculate the perimeter of the circle

```python
def perimetr(r):
```
- The program returns the perimeter of the circle
```python
return 2 * math.pi * r
```

### Example call:
```python
import math

def area(r):
    return math.pi * r * r

def perimetr(r):
    return 2 * math.pi * r

int r = 5
print(area(r))
print(perimetr(r))
```
## Rectangle
```python
def area(a, b):
    return a * b

def perimetr(a, b):
    return 2 * (a + b)
```
- Takes two numbers: a and b - the length and width of the rectangle to calculate its area

```python
def area(a, b):
```
- Returns the area of a rectangle

```python
return a * b
```
- The function for calculating the perimeter takes two numbers: a and b - the length and width of the rectangle to calculate its perimeter
```python
def perimetr(a, b):
```
- Returns the perimeter of a rectangle
```python
return 2 * (a + b)
```
### Example call:
```python
def area(a, b):
    return a * b

def perimetr(a, b):
    return 2 * (a + b)

int a = 5
int b = 6
print(area(a, b))
print(perimetr(a, b))
```
## Square
```python
def area(a):
    return a * a

def perimetr(a):
    return 4 * a
```
- The function for calculating the area takes the number a - the side of the square to calculate its area
```python
def area(a):
```
- Returns the area of a square

```python
return a * a
```
- The function for calculating the perimeter takes the number a - the side of the square to calculate its perimeter

```python
def perimetr(a):
```
- Returns the perimetr of a square
```python
return 4 * a
```
### Example call:
```python
def area(a):
    return a * a

def perimetr(a):
    return 4 * a

int a = 10
print(area(a))
print(perimetr(a))
```
## Triangle
```python
def area(a, h):
    return a * h / 2

def perimetr(a, b, c):
    return a + b + c
```
- The function for calculating the area takes two numbers: a and h - the side and height of the triangle to calculate its area

```python
def area(a, h):
```
- Returns the area of a triangle

```python
return a * h / 2
```
- The function for calculating the perimeter takes three numbers: a, b, c - sides of the triangle
```python
def perimetr(a, b, c):
```
- Returns the perimetr of a triangle
```python
return a + b + c
```
### Example call:
```python
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
```
### Unit Tests
#### Rectangle
|  Type of Operation  |      Tests Name      | Input Data |  Excepted Result  |         Result          |
|:-------------------:|:--------------------:|:----------:|:-----------------:|:-----------------------:|
|        Area         |    area_testcases    |    10 2     |        20         | $${\color{green}True}$$ |
|      Perimetr       |  perimetr_testcases  |    a 2     |     TypeError     | $${\color{green}True}$$ |            
|        Area         |    area_testcases    |   -3 10    |    ValueError     | $${\color{green}True}$$ |         

#### Triangle
| Type of Operation |      Tests Name      | Input Data | Excepted Result |         Result          |
|:-----------------:|:--------------------:|:----------:|:---------------:|:-----------------------:|
|       Area        |    area_testcases    |   7 8      |       28        | $${\color{green}True}$$ |
|     Perimetr      |  perimetr_testcases  |   a b c    |    TypeError    | $${\color{green}True}$$ |            
|     Perimetr      |  perimetr_testcases  |  -23 1 4   |   ValueError    | $${\color{green}True}$$ |    

#### Square
| Type of Operation |      Tests Name      | Input Data | Excepted Result |         Result          |
|:-----------------:|:--------------------:|:----------:|:---------------:|:-----------------------:|
|       Area        |    area_testcases    |     a      |    TypeError    | $${\color{green}True}$$ |
|     Perimetr      |  perimetr_testcases  |    100     |       400       | $${\color{green}True}$$ |            
|       Area        |    area_testcases    |     -2     |   ValueError    | $${\color{green}True}$$ |         

#### Circle
| Type of Operation |      Tests Name      | Input Data | Excepted Result |         Result          |
|:-----------------:|:--------------------:|:----------:|:---------------:|:-----------------------:|
|       Area        |    area_testcases    |     5      |     10 * pi     | $${\color{green}True}$$ |
|     Perimetr      |  perimetr_testcases  |     p      |    TypeError    | $${\color{green}True}$$ |            
|       Area        |    area_testcases    |    1000    | 1000000 * $\pi$ | $${\color{green}True}$$ |         


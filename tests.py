import unittest
import math
import rectangle
import square
import circle
import triangle

class PerimetrAreaTestCase(object):

    def test_perimetr(self):
        for inp, outp in self.perimetr_testcases:
            result = self.module.perimetr(*inp)
            self.assertEqual(
                result,
                outp,
                f'{self.module.__name__}:perimetr\t{inp=} excepted={outp} returned={result}'
            )

    def test_area(self):
        for inp, outp in self.area_testcases:
            result = self.module.area(*inp)
            self.assertEqual(
                result,
                outp,
                f'{self.module.__name__}:area\t{inp=} exсepted={outp} returned={result}'
            )


class RectangleTestCase(PerimetrAreaTestCase, unittest.TestCase):
    def setUp(self):
        self.module = rectangle
        
        self.area_testcases = (
            ((10, 2), 20), 
            (("a", 3), TypeError), 
            ((-3, 10), ValueError),
            ((100, 100), 10000),
            ((1000000, 1000000), 1000000000000),
            ((2, 0), ValueError)
        )

        self.perimetr_testcases = (
            (('a', 2), TypeError),
            ((5, 4), 18),
            ((2, 4), 12),
            ((-1, 10), ValueError),
            ((10, 10), 40),
            ((10000, 100000), 220000)
        )

class TriangleTestCase(PerimetrAreaTestCase, unittest.TestCase):
    def setUp(self):
        self.module = triangle
        
        self.area_testcases = (
            ((-10, 8), ValueError),
            (('b', 10), TypeError),
            ((7, 8), 28),
            ((30000, 1000000), 15000000000),
            ((3, 0), ValueError)
        )

        self.perimetr_testcases = (
            (('a', 'b', 'c'), TypeError),
            ((-23, 1, 4), ValueError),
            ((200000, 200000, 30000000000), 30000400000),
            ((9, 8, 4), 21),
            ((1000, 1000, 1000), 3000),
        )

class SquareTestCase(PerimetrAreaTestCase, unittest.TestCase):
    def setUp(self):

        self.module = square

        self.area_testcases = (
            (('a', ), TypeError),
            ((-2, ), ValueError),
            ((10, ), 100),
            ((-20000, ), ValueError),
            ((1000000, ), 1000000000000),
        )

        self.perimetr_testcases = (
            ((-9, ), ValueError),
            ((100, ), 400),
            ((15, ), 60),
            ((4.5, ), 18),
            ((10000, ), 40000),
            (('p', ), TypeError)
        )
class CircleTestCase(PerimetrAreaTestCase, unittest.TestCase):
    def setUp(self):
        
        self.module = circle

        self.perimetr_testcases = (
            ((-123, ), ValueError),
            (('p', ), TypeError),
            ((1000, ), 2000 * math.pi),
            ((0, ), ValueError),
            ((5, ), 10 * math.pi)

        )

        self.area_testcases = (
            ((3, ), math.pi * 9),
            (('f', ), TypeError),
            ((1000, ), math.pi * 1000000),
            ((0, ), ValueError),
            ((1000000, ), math.pi * 1000000000000)
        )

        

if __name__ == "__main__":
    unittest.main()

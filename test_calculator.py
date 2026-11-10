import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    
    def test_add(self): # 3 assertions
        self.assertEqual(add( 5, 2), 7)
        self.assertEqual(add( -1, 7), 6)
        self.assertEqual(add( 100, 87), 187)

    def test_subtract(self): # 3 assertions
        self.assertEqual(subtract( 5, 2), 3)
        self.assertEqual(subtract( 76, -2), 78)
        self.assertEqual(subtract( -39, 5), -44)
    
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul( 5, 2), 10)
        self.assertEqual(mul( -1, 7), -7)
        self.assertEqual(mul( 100, 87), 8700)

    def test_divide(self): # 3 assertions
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)
        with self.assertRaises(ZeroDivisionError):
            div(0, 0)
        with self.assertRaises(ZeroDivisionError):
            div(0, -5)

    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(0, 5)

    def test_hypotenuse(self): # 3 assertions
        with self.assertRaises(TypeError):
            hypotenuse(5, "b")
        with self.assertRaises(TypeError):
            hypotenuse("a", 5)
        with self.assertRaises(TypeError):
            hypotenuse("a", "b")

    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    def test_logarithm(self): # 3 assertions
        self.assertEqual(logarithm( 10, 100), 2)
        self.assertEqual(logarithm( 2, 8), 3)
        self.assertEqual(logarithm( 3, 729), 6)

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(-3, 4)
    
    def test_sqrt(self): # 3 assertions
        with self.assertRaises(ValueError):
           square_root(-5)
        with self.assertRaises(ValueError):
           square_root(-1)
        with self.assertRaises(ValueError):
           square_root(-100)

# Do not touch this
if __name__ == "__main__":
    unittest.main()
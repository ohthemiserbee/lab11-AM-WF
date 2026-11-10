import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    def test_multiply(self): # 3 assertions
        with self.assertRaises(TypeError):
            mul(5, "b")
        with self.assertRaises(TypeError):
            mul("a", 5)
        with self.assertRaises(TypeError):
            mul("a", "b")

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
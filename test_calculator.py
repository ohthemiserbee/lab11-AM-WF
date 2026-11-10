import unittest
from calculator import *

class TestCalculator(unittest.TestCase):

    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add( 5, 2), 7)
        self.assertEqual(add( -1, 7), 6)
        self.assertEqual(add( 100, 87), 187)
    #     fill in code

    def test_subtract(self): # 3 assertions
        self.assertEqual(sub( 5, 2), 3)
        self.assertEqual(sub( 76, -2), 78)
        self.assertEqual(sub( -39, 5), -44)
    #     fill in code
    # ##########################

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


    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code

    def test_logarithm(self): # 3 assertions
        self.assertEqual(sub( 10, 100), 2)
        self.assertEqual(sub( 2, 8), 3)
        self.assertEqual(sub( 3, 729), 6)
    #     fill in code

    def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
    #     fill in code
    # ##########################
        with self.assertRaises(ValueError):
            log(-3, 4)
    ######## Partner 1
    # def test_log_invalid_argument(self): # 1 assertion
    #     # call log function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     logarithm(0, 5)
    #     fill in code

    # def test_hypotenuse(self): # 3 assertions
    #     fill in code

    # def test_sqrt(self): # 3 assertions
    #     # Test for invalid argument, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #    square_root(NUM)
    #     # Test basic function
    #     fill in code
    ##########################

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
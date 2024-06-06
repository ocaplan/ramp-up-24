import unittest
from nextnum_very_easy import *
from return_the_sum_of_two_numbers_very_easy import *
from find_the_discount_easy import *
from radians_to_degrees_easy import *
from length_of_number_medium import *
from sum_of_odd_and_even_medium import *
from factorial_of_factorials_hard import *
from powerful_numbers_hard import *


class MyTestCase(unittest.TestCase):
    def test_nextnum(self):
        self.assertEqual(1, nextnum(0))
        self.assertEqual(10, nextnum(9))
        self.assertEqual(-2, nextnum(-3))
    def test_return_the_sum_of_two_numbers(self):
        self.assertEqual(5, sum_of_two_numbers(3, 2))
        self.assertEqual(-9, sum_of_two_numbers(-3, -6))
        self.assertEqual(10, sum_of_two_numbers(7, 3))
    def test_find_the_discount(self):
        self.assertEqual(750, find_the_discount(1500, 50))
        self.assertEqual(71.2, find_the_discount(89, 20))
        self.assertEqual(25, find_the_discount(100, 75))
    def test_radians_to_degrees(self):
        self.assertEqual(57.3, radians_to_degrees(1))
        self.assertEqual(1145.9, radians_to_degrees(20))
        self.assertEqual(2864.8, radians_to_degrees(50))
    def test_length_of_number(self):
        self.assertEqual(2, length_of_number(10))
        self.assertEqual(4, length_of_number(5000))
        self.assertEqual(1, length_of_number(0))
    def test_sum_of_odd_and_even(self):
        self.assertEqual([12,9], sum_of_odd_and_even([1,2,3,4,5,6]))
    def test_factorial_of_factorials(self):
        self.assertEqual(288, factorial_of_factorials(4))
        self.assertEqual(34560, factorial_of_factorials(5))
        self.assertEqual(24883200, factorial_of_factorials(6))
    def test_powerful_numbers(self):
        self.assertTrue(powerful_numbers(36))


if __name__ == '__main__':
    unittest.main()

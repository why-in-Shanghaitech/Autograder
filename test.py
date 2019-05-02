#=============================================================================#
#                           Homework 5: pyFraction                            #
#       SI 100B: Introduction to Information Science and Technology B         #
#                     Spring 2019, ShanghaiTech University                    #
#                     Author: Diao Zihao <hi@ericdiao.com>                    #
#                         Last motified: 04/12/2019                           #
#=============================================================================#
# test.py - test your implementation.
# PLEASE NOTE: Teatcases here are different from those in the auto-grader. Only
# results of the testcases in the auto-grader will be considered valid and will
# count for your final score.

import unittest
import pyfraction

# Feel Free to motify the testcases below to create your own testcases.


class TestTask1(unittest.TestCase):

    def setUp(self):
        self.posFraction = pyfraction.Fraction(1, 2)
        self.negFraction = pyfraction.Fraction(1, 2, sign="-")

    def testInit(self):
        self.assertEqual(self.posFraction.get_numerator(), 1)
        self.assertEqual(self.posFraction.get_denominator(), 2)
        self.assertTrue(self.posFraction.is_nonnegative())
        self.assertEqual(self.negFraction.get_numerator(), 1)
        self.assertEqual(self.negFraction.get_denominator(), 2)
        self.assertFalse(self.negFraction.is_nonnegative())


class TestTask2(unittest.TestCase):

    def setUp(self):
        self.zero = pyfraction.Fraction(0, 1)
        self.neg = pyfraction.Fraction(-1, 1)
        self.pos = pyfraction.Fraction(1, 1)

    def testOperations(self):
        self.assertTrue(self.zero < self.pos)
        self.assertTrue(self.pos > self.neg)
        self.assertTrue((self.neg + self.pos) == self.zero)
        self.assertEqual(self.zero - self.pos, self.neg)
        self.assertEqual(abs(self.neg), self.pos)


class TestTask3(unittest.TestCase):

    def setUp(self):
        self.zero_point_five = pyfraction.Fraction(1, 2)
        self.zero = pyfraction.Fraction(0, 1)

    def testToFloat(self):
        self.assertEqual(self.zero_point_five.to_float(), 0.5)

    def testFromInteger(self):
        self.assertEqual(pyfraction.Fraction.from_integer(0), self.zero)

    def testFromString(self):
        self.assertEqual(pyfraction.Fraction.from_string(
            "\\frac{1}{2}"), self.zero_point_five)


class TestTask4(unittest.TestCase):

    def setUp(self):
        self.result = pyfraction.Fraction(45, 1)

    def testCalculator(self):
        self.assertEqual(pyfraction.evaluate_postfix_expr(
            "1 2 + 3 * 5 *"), self.result)


if __name__ == '__main__':
    unittest.main()

#=============================================================================#
#                           Homework 5: pyFraction                            #
#       SI 100B: Introduction to Information Science and Technology B         #
#                     Spring 2019, ShanghaiTech University                    #
#                     Author: Diao Zihao <hi@ericdiao.com>                    #
#                         Last motified: 04/12/2019                           #
#=============================================================================#
# pyfraction.py - write your code here.

#=============================================================================#
# Some exceptions pre-defined exceptions for you.


class BaseFractionError(BaseException):
    '''
    The base class for the pyFraction moudule you wrote. All other Exceptions
    shall inherits from this class.
    '''
    pass


class FractionDividedByZeroError(BaseFractionError):
    '''
    You shall raise this exception when the user input asked your program to
    divide a number by 0. Quite similar to the standard `ZeroDivisionError`.
    '''
    pass


class FractionNonRationalError(BaseFractionError):
    '''
    You shall raise this exception when the user input asked your program to
    deal with a non-rational number.
    '''
    pass


class FractionNonIntegerError(BaseFractionError):
    '''
    You shall raise this exception when the user input asked your program to
    deal with a non-integer input.
    '''
    pass

#=============================================================================#

## DEFINE YOUR OWN EXCEPTIONS HERE ##

#=============================================================================#

#=============================================================================#
# The `Fraction` class that you need to deal with.


class Fraction:
    '''
    The class Fraction you needs to implement. See the comments below for
    implementation detail.
    '''

    def __init__(self, numerator, denominator, sign='+'):
        '''
        Initialize your Fraction instance. You could choice your own
        implementation as long as it meets the requirements in README.
        '''
        raise NotImplementedError
        ## YOUR CODE HERE ##

    def __str__(self):
        '''
        Return a string representation of this number when using print(num).
        This method is implemented for you.
        '''
        return "{}\\frac{{{}}}{{{}}}".format('' if self.is_nonnegative() else '-',
            self.get_numerator(), self.get_denominator())

    def get_numerator(self):
        '''
        Return the numerator of this fraction.
        '''
        raise NotImplementedError
        ## YOUR CODE HERE ##

    def get_denominator(self):
        '''
        Return the denominator of this fraction.
        '''
        raise NotImplementedError
        ## YOUR CODE HERE ##

    def is_nonnegative(self):
        '''
        Return True if this fraction is postive or zero.
        Return False if it is negative.
        '''
        raise NotImplementedError
        ## YOUR CODE HERE ##

    def __neg__(self):
        '''
        Return `-self`.
        '''
        raise NotImplementedError
        ## YOUR CODE HERE ##

    def __eq__(self, other):
        '''
        If `self` equals to `other`.
        Return `True` on `self` == `other` as a fraction, False otherwise.
        '''
        raise NotImplementedError
        ## YOUR CODE HERE ##

    def __ne__(self, other):
        '''
        If `self` equals to `other`.
        Return `True` on `self` != `other` as a fraction, False otherwise.
        '''
        raise NotImplementedError
        ## YOUR CODE HERE ##

    def __lt__(self, other):
        '''
        If `self` is less than `other`.
        Return `True` on `self` < `other` as a fraction, False otherwise.
        '''
        raise NotImplementedError
        ## YOUR CODE HERE ##

    def __le__(self, other):
        '''
        If `self` is less than or equals to `other`.
        Return `True` on `self` <= `other` as a fraction, False otherwise.
        '''
        raise NotImplementedError
        ## YOUR CODE HERE ##

    def __gt__(self, other):
        '''
        If `self` is greater than `other`.
        Return `True` on `self` > `other` as a fraction, False otherwise.
        '''
        raise NotImplementedError
        ## YOUR CODE HERE ##

    def __ge__(self, other):
        '''
        If `self` is greater than or equals to `other`.
        Return `True` on `self` >= `other` as a fraction, False otherwise.
        '''
        raise NotImplementedError
        ## YOUR CODE HERE ##

    def __abs__(self):
        '''
        return the absolute value of this number.
        The return value should also be a Fraction instance.
        '''
        raise NotImplementedError
        ## YOUR CODE HERE ##

    def __add__(self, other):
        '''
        return the result of `self + other` as another Fraction instance.
        '''
        raise NotImplementedError
        ## YOUR CODE HERE ##

    def __sub__(self, other):
        '''
        return the result of `self - other` as another Fraction instance.
        '''
        raise NotImplementedError
        ## YOUR CODE HERE ##

    def __mul__(self, other):
        '''
        return the result of `self * other` as another Fraction instance.
        '''
        raise NotImplementedError
        ## YOUR CODE HERE ##

    def __truediv__(self, other):
        '''
        return the result of `self / other` as another Fraction instance.
        '''
        raise NotImplementedError
        ## YOUR CODE HERE ##

    def to_float(self):
        '''
        return the approximate float representaion of the Fraction instance
        '''
        raise NotImplementedError
        ## YOUR CODE HERE ##

    @staticmethod
    def from_string(string):
        '''
        return a Fraction instance built from a string. See the
        specification in README for more information.
        '''
        raise NotImplementedError
        ## YOUR CODE HERE ##

    @staticmethod
    def from_integer(integer):
        '''
        return a Fraction instance built from a integer. See the
        specification in README for more information.
        '''
        raise NotImplementedError
        ## YOUR CODE HERE ##

#=============================================================================#

def evaluate_postfix_expr(expr):
    '''
    Implement your postfix calculator here.
    '''
    raise NotImplementedError
    ## YOUR CODE HERE ##


#=============================================================================#

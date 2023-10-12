"""
- Make use of the appropriate assert methods in unit tests.
- The unittest.TestCase class in Python's standard library includes a number
of helpful assert methods to be used when writing tests.
"""


import unittest


# Harmful solution
# class Test(unittest.TestCase):
#     def test_adding_positive_ints(self):
#         """Does adding together two positive integers work?"""
#         self.assertTrue(my_addition(2, 2) == 4)

#     def test_increment(self):
#         """Does increment return a value greater than what was passed as an
#         argument?"""
#         self.assertTrue(increment(1) > 1)

#     def test_divisors_of_prime_number(self):
#         self.assertTrue(get_divisors(11) is None)


# Idiomatic solution
def my_addition(first_parameter, second_parameter):
    """
    Return the result of adding two numbers.

    Parameters:
        first_parameter (int): The first number.
        second_parameter (int): The second number.

    Returns:
        int: The sum of the two input numbers.
    """

    return first_parameter + second_parameter


def increment(parameter):
    """
    Return the value greater than the input number.

    Parameters:
        parameter (int): The input number.

    Returns:
        int: The input number incremented by 1.
    """

    return parameter + 1


def get_divisors(exam_parameter):
    """
    Return the divisors of a number.

    Parameters:
        exam_parameter (int): The input number.

    Returns:
        list: A list of divisors of the input number. An empty list is
        returned for prime numbers.
    """

    return []


class Test(unittest.TestCase):
    def test_adding_positive_ints(self):
        """
        Does adding together two positive integers work?
        """

        self.assertEqual(my_addition(2, 2), 4)

    def test_increment(self):
        """
        Does increment return a value greater than what was passed as an
        argument?
        """

        self.assertGreater(increment(1), 1)

    def test_divisors_of_prime_number(self):
        """
        Does get_divisors return None for a prime number?
        """

        self.assertIsNone(get_divisors(11))

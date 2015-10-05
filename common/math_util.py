
import unittest
from math import sqrt, floor


def get_divisors(num, proper=False, debug=False):
    """
    Given a number, return a list of its divisors.
    If "proper" is False, returns all divisors.
    Example:  28 => [1, 2, 4, 7, 14, 28]
    If "proper" is True, returns only the proper divisors.
    Example:  28 => [1, 2, 4, 7, 14]
    """
    divisors = [1, num] if num > 1 else [1] if num == 1 else []
    i = 2

    # Increment, looking for divisors, until reaching the limit of 1/2 the number.
    while i <= floor(sqrt(num)):
        if num % i == 0:
            num_divisors = len(divisors)

            divisors.append(i)
            divisors.append(num / i)

            if debug and num_divisors != len(divisors):
                print "i: {} - current divisors: {}".format(i, divisors)

        i += 1

    # Sort the divisors and add them to the cache.
    divisors = sorted(list(set(divisors)))
    if proper:
        # If proper divisors are requested, remove the number itself from the divisors.
        divisors = divisors[:-1]
    return divisors


def is_prime(num):
    """
    Returns True if number is a prime number.
    """
    if num <= 1:
        return False

    return len(get_divisors(num)) == 2


def is_perfect(num):
    """
    Return True if a number is perfect, i.e. if the sum of the number's proper divisors
    is equal to the number itself.
    """
    return sum(get_divisors(num, proper=True)) == num


def is_abundant(num):
    """
    Return True if a number is abundant, i.e. if the sum of the number's proper divisors
    is greater than the number itself.
    """
    return sum(get_divisors(num, proper=True)) > num


class TestMath(unittest.TestCase):

    def test_get_factors(self):
        self.assertEqual(get_divisors(0), [])
        self.assertEqual(get_divisors(1), [1])
        self.assertEqual(set(get_divisors(28)), set([1, 2, 4, 7, 14, 28]))
        self.assertEqual(set(get_divisors(28, proper=True)), set([1, 2, 4, 7, 14]))

    def test_prime(self):
        self.assertFalse(is_prime(0))
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(10000))
        self.assertTrue(is_prime(103483))
        self.assertTrue(is_prime(104729))

    def test_is_perfect(self):
        self.assertFalse(is_perfect(27))
        self.assertTrue(is_perfect(28))

    def test_is_abundant(self):
        self.assertFalse(is_abundant(4))
        self.assertTrue(is_abundant(12))


if __name__ == '__main__':
    unittest.main()
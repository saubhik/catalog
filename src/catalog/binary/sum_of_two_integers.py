import unittest


class SumOfTwoIntegers:
    """
    Problem: https://leetcode.com/problems/sum-of-two-integers/
    """

    @staticmethod
    def get_sum(a: int, b: int) -> int:
        """
        Sums integers a and b without using operators + & -.

        Args:
            a: first integer.
            b: second integer.

        Returns:
            Sum of a and b.

        Notes:
            Uses XOR for addition.
            Uses AND for carry overs.
            Do not forget to shift carry to left.
        """
        while b != 0:
            carry = a & b
            a = a ^ b
            b = carry << 1

        return a


class Test(unittest.TestCase):
    def test_get_sum(self):
        obj = SumOfTwoIntegers()
        self.assertEqual(47, obj.get_sum(32, 15))
        self.assertEqual(47, obj.get_sum(15, 32))
        self.assertEqual(0, obj.get_sum(0, 0))

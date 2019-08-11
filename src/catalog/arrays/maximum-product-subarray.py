# Maximum Product Subarray
#
# https://leetcode.com/problems/maximum-product-subarray/
#
# Example:
# All negatives:
#                  -2 | -3 | -4
# max_ending_here: -2 |  6 | 12
# min_ending_here: -2 | -3 | -24
# max_so_far     : -2 |  6 | 12
#
# Mixture of positives & negatives:
#                  -2 | 5   | -3
# max_ending_here: -2 | 5   | 30
# min_ending_here: -2 | -10 | -15
# max_so_far     : -2 | 5   | 30
#
# Space: O(1)
# Time : O(n)
#
# Also known as Kadane's Algorithm


from typing import List
import unittest


def max_product(nums: List[int]) -> int:

    if not nums:
        raise ValueError("nums must not be empty")

    max_ending_here = nums[0]
    min_ending_here = nums[0]
    max_so_far = nums[0]

    for i in range(1, len(nums)):

        prev_max_ending_here = max_ending_here
        max_ending_here = max(
            prev_max_ending_here * nums[i], nums[i], min_ending_here * nums[i]
        )
        min_ending_here = min(
            prev_max_ending_here * nums[i], nums[i], min_ending_here * nums[i]
        )

        if max_ending_here > max_so_far:
            max_so_far = max_ending_here

    return max_so_far


class TestMaxProduct(unittest.TestCase):
    def test_max_product(self):
        self.assertEqual(12, max_product([-2, -3, -4]))
        self.assertEqual(30, max_product([-2, 5, -3]))
        self.assertEqual(0, max_product([0]))
        self.assertEqual(0, max_product([-2, 0, -10]))


if __name__ == "__main__":
    unittest.main()

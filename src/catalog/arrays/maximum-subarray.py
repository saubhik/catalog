# Maximum Subarray
# https://leetcode.com/problems/maximum-subarray/
#
# Examples:
#                  4 | 2 | -3 | 5
# max_ending_here: 4 | 6 | 3  | 8
# max_so_far     : 4 | 6 | 6  | 8
#
# Space: O(1)
# Time : O(n)

from typing import List
import unittest


def max_sub_array(nums: List[int]) -> int:

    if not nums:
        raise ValueError("nums must not be empty")

    max_ending_here = nums[0]
    max_so_far = nums[0]

    for i in range(1, len(nums)):
        max_ending_here = max(max_ending_here + nums[i], nums[i])
        if max_ending_here > max_so_far:
            max_so_far = max_ending_here

    return max_so_far


class Test(unittest.TestCase):
    def test_max_sub_array(self):
        self.assertEqual(8, max_sub_array([4, 2, -3, 5]))
        self.assertEqual(10, max_sub_array([-1, -1, -2, 5, -10, 10]))


if __name__ == "__main__":
    unittest.main()

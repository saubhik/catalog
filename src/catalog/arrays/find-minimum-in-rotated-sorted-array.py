# Find Minimum In Rotated Sorted Array
# Assume no duplicates.
#
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
#
# Example:
#
# 3, 4, 5, 1, 2
# answer: 1
#
# We apply a modified version of binary search.
# Iteration 1:
# lo : 0
# hi : 4
# mid: 2
# Numbers:
# nums[lo]  = 3
# nums[mid] = 5
# nums[hi]  = 2
#
# Hypothesis: If nums[i] < nums[j], where i < j, then nums[i..j] is sorted.
# Proof: Suppose not. Then there is k, such that i < k < j, and nums[k] > nums[k + 1].
# Since there is a single rotation point, we have two sorted sequences:
# 1. nums[i...k]
# 2. nums[k+1...j]
# Since we have a rotation, nums[k+1...j], nums[i...k] are in sorted order.
# This implies nums[j] < nums[i], which is a contradiction.
#
# Based on above hypothesis we can focus on the half in which the bounding numbers are in opposite order.
# So our rotation point lies in nums[mid...hi].
#
# Iteration 2:
# lo  : 2
# hi  : 4
# mid : 3
# Numbers:
# nums[lo]  = 5
# nums[mid] = 1
# nums[hi]  = 2
# We focus on nums[lo...mid].
#
# Iteration 3:
# lo  : 2
# hi  : 3
# mid : 2
# Numbers:
# nums[lo]  = 5
# nums[mid] = 5
# nums[hi]  = 1
# Since, lo & mid are same, we go ahead with hi.
#
# Space; O(1)
# Time : O(logN)

from typing import List
import unittest


def find_min(nums: List[int]) -> int:

    if not nums:
        raise ValueError("nums should not be empty")

    lo, hi = 0, len(nums) - 1

    while True:

        mid = lo + ((hi - lo) // 2)

        if lo == mid:
            break

        if nums[mid] > nums[hi]:
            lo = mid
        else:
            # Supports sorted arrays too
            hi = mid

    return min(nums[hi], nums[lo])


class Test(unittest.TestCase):
    def test_find_min(self):
        self.assertEqual(1, find_min([3, 4, 5, 1, 2]))
        self.assertEqual(1, find_min([4, 1, 2, 3]))
        self.assertEqual(2, find_min([2, 3, 4, 5, 8]))


if __name__ == "__main__":
    unittest.main()

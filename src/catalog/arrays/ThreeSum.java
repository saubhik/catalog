package catalog.arrays;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/*
Given: An array of n integers.

Problem: Find all unique triplets which sum to zero.

Algorithm:
- Sorting based algorithm:
Sort and then use two pointers.
 */
public class ThreeSum {
  public List<List<Integer>> threeSum(int[] nums) {
    List<List<Integer>> answers = new ArrayList<>();
    Arrays.sort(nums);
    int n = nums.length, left, right, sum;
    for (int i = 0; i < n - 2; i++) {
      if (nums[i] > 0) break;
      if (i > 0 && nums[i - 1] == nums[i]) {
        continue;
      }
      left = i + 1;
      right = n - 1;
      while (left < right) {
        sum = nums[i] + nums[left] + nums[right];
        if (sum < 0) {
          left++;
        } else if (sum > 0) {
          right--;
        } else {
          answers.add(Arrays.asList(nums[i], nums[left], nums[right]));
          left++;
          right--;
          while (left < right && nums[left] == nums[left - 1]) left++;
          while (left < right && nums[right] == nums[right + 1]) right--;
        }
      }
    }
    return answers;
  }
}

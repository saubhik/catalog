package catalog.arrays;

/*
Given: n non-negative integers, each of which represents bars {(i,0),(i,ai)} for 1 <= i <= n.

Problem: max area of water between two such vertical bars.

Algorithm:
- Two pointers, one at start and one at end.
- Record the current area, and then move the pointer pointing to the shorter bar.
- Completes when pointers meet.

Complexity:
- time: O(n)
- space: O(1)

Correctness:
At each step, we have found the maximum area possible with the shorter bar. No need to consider the shorter bar again.
Hence it makes sense to move the pointer pointing to the shorter bar.
*/
public class ContainerWithMostWater {
  public int maxArea(int[] height) {
    int left = 0, right = height.length - 1, maxArea = 0;
    while (left < right) {
      maxArea = Math.max(maxArea, Math.min(height[left], height[right]) * (right - left));
      if (height[left] < height[right]) {
        left++;
      } else {
        right--;
      }
    }
    return maxArea;
  }
}

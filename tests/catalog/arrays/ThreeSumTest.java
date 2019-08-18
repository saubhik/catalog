package catalog.arrays;

import java.util.Arrays;
import java.util.Collections;

import static org.junit.jupiter.api.Assertions.assertEquals;

class ThreeSumTest {
  @org.junit.jupiter.api.Test
  void testThreeSum() {
    ThreeSum threeSum = new ThreeSum();
    assertEquals(
        Collections.singletonList(Arrays.asList(-1, 0, 1)),
        threeSum.threeSum(new int[] {-1, -1, -1, 0, 1, 1, 1}));
    assertEquals(
        Arrays.asList(Arrays.asList(-1, -1, 2), Arrays.asList(-1, 0, 1)),
        threeSum.threeSum(new int[] {-1, 0, 1, 2, -1, -4}));
    assertEquals(
        Arrays.asList(Arrays.asList(-2, 0, 2), Arrays.asList(-2, 1, 1)),
        threeSum.threeSum(new int[] {-2, 0, 1, 1, 2}));
  }
}

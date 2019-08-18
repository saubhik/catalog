package catalog.arrays;

import static org.junit.jupiter.api.Assertions.assertEquals;

class ContainerWithMostWaterTest {

  @org.junit.jupiter.api.Test
  void testMaxArea() {
    ContainerWithMostWater containerWithMostWater = new ContainerWithMostWater();
    assertEquals(containerWithMostWater.maxArea(new int[] {1, 8, 6, 2, 5, 4, 8, 3, 7}), 49);
  }
}

package catalog.graphs.clonegraph.similars;

import static org.junit.jupiter.api.Assertions.*;

class CloneLinkedListTest {

  @org.junit.jupiter.api.Test
  void testClone() {
    CloneLinkedList.Node first = new CloneLinkedList.Node(1);
    CloneLinkedList.Node second = new CloneLinkedList.Node(2);
    CloneLinkedList.Node third = new CloneLinkedList.Node(3);
    CloneLinkedList.Node fourth = new CloneLinkedList.Node(4);
    CloneLinkedList.Node fifth = new CloneLinkedList.Node(5);

    // Define the next pointers
    first.next = second;
    second.next = third;
    third.next = fourth;
    fourth.next = fifth;

    // Define the random pointers
    first.random = third;
    second.random = first;
    third.random = fifth;
    fourth.random = fifth;
    fifth.random = second;

    CloneLinkedList.Node clonedNode = CloneLinkedList.clone(first);

    assertTrue(first.equals(clonedNode));

    first.next.next.next.next = null;
    assertTrue(first.equals(CloneLinkedList.clone(first)));

    // random pointers do not match
    first.next.next.next.next = new CloneLinkedList.Node(5);
    assertFalse(first.equals(clonedNode));

    // everything matches
    first.next.next.next.next = fifth;
    assertTrue(first.equals(clonedNode));
  }
}

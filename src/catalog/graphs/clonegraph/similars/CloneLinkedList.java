package catalog.graphs.clonegraph.similars;

/**
 * Clone doubly linked list with next & random pointers.
 *
 * <p>Given: A double linked list, with one pointer of each node pointing to the next node (like in
 * a single linked list). The second pointer can point to any node in the list and not just the
 * previous node. We will call such a linked list as a linked list with a next and arbitrary (or
 * random) pointers. Assume every node holds a unique integer data.
 *
 * <p>Problem: Duplicate / clone / deep copy this list.
 *
 * <p>Time Complexity: O(n), Additional/Auxiliary Space Complexity: O(1)
 */
public class CloneLinkedList {

  static class Node {
    int data;
    Node next, random;

    Node(int x) {
      data = x;
      next = random = null;
    }

    /*
    We assume every node has a different value, which serves like it's id.
     */
    public boolean equals(Node node) {
      Node otherCurrent = node;
      Node current = this;
      while (otherCurrent != null) {
        if (current == null) {
          return false;
        }

        // check data
        if (current.data != otherCurrent.data) {
          return false;
        }

        // check random pointers - 4 cases
        if (current.random == null) {
          if (otherCurrent.random == null) {
            continue;
          } else {
            return false;
          }
        } else {
          if (otherCurrent.random == null) {
            return false;
          } else {
            // check data at random pointers
            if (current.random.data != otherCurrent.random.data) {
              return false;
            }
          }
        }

        otherCurrent = otherCurrent.next;
        current = current.next;
      }
      return current == null;
    }
  }

  /*
  Time: O(n)
  Auxiliary Space: O(1)
  */
  public static Node clone(Node head) {
    Node clonedHead = new Node(head.data);

    // Clone with only next pointers
    Node clonedPrevious = clonedHead;
    Node current = head.next;
    while (current != null) {
      Node clonedCurrent = new Node(current.data);
      clonedPrevious.next = clonedCurrent;
      current = current.next;
      clonedPrevious = clonedCurrent;
    }

    // Add the random pointers
    current = head;
    Node clonedCurrent = clonedHead;
    while (current != null) {
      clonedCurrent.random = current.random;
      current = current.next;
      clonedCurrent = clonedCurrent.next;
    }
    return clonedHead;
  }

  private static void printList(Node node) {
    Node current = node;
    while (current != null) {
      System.out.println("Data = " + current.data + ", Random = " + current.random.data);
      current = current.next;
    }
  }

  public static void main(String[] args) {
    Node first = new Node(1);
    Node second = new Node(2);
    Node third = new Node(3);
    Node fourth = new Node(4);
    Node fifth = new Node(5);

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

    printList(first);
    System.out.println();
    printList(clone(first));
  }
}

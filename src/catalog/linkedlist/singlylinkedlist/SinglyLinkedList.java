package catalog.linkedlist.singlylinkedlist;

/**
 * Linked list: A linear data structure, whose elements are not stored in contiguous locations; the elements are linked
 * using pointers.
 *
 * WHY?
 * 1. Dynamic size: Size of an array has to be known in advance. Allocated memory is equal to upper limit irrespective
 * of usage.
 * 2. Easy insertion/deletion: To maintain sorted order in an array, lot of shifts required.
 *
 * WHY NOT?
 * 1. No random access: Cannot do efficient binary search. TODO: Implementation?
 * 2. Extra memory for pointer required with each element of the list.
 * 3. Not cache-friendly: Arrays have locality of reference.
 */
public class SinglyLinkedList {
    Node head;

    static class Node {
        int data;
        Node next; // initialised to null

        Node(int d) {
            data = d;
        }
    }

    /*
    Traverse a singly linked list.
     */
    public void traverse() {
        Node current = head;
        while (current != null) {
            System.out.print(current.data + " ");
            current = current.next;
        }
    }

    public static void main(String[] args) {
        SinglyLinkedList linkedList = new SinglyLinkedList();

        linkedList.head = new Node(1);
        Node second = new Node(2);
        Node third = new Node(3);

        linkedList.head.next = second;
        second.next = third;

        linkedList.traverse();
    }
}

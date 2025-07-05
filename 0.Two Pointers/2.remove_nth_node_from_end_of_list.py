#!/usr/bin/env python3
"""
remove_nth_last_node.py

Two ways to remove the Nth node from the end of a singly linked list:

1. length-based two-pass (fixed off-by-one)
2. one-pass two-pointer

Usage:
    python remove_nth_last_node.py "[1, 2, 3, 4, 5]" 2
    # Removes the 2nd last node (4), printing both results.
"""

import sys
import ast

class ListNode:
    """Simple singly-linked-list node."""
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def build_list(arr):
    """Builds a linked list from a Python list and returns its head."""
    dummy = ListNode(0)
    curr = dummy
    for x in arr:
        curr.next = ListNode(x)
        curr = curr.next
    return dummy.next

def list_to_pylist(head):
    """Converts a linked list back into a Python list for easy printing."""
    arr = []
    curr = head
    while curr:
        arr.append(curr.val)
        curr = curr.next
    return arr

def remove_nth_last_node_length(head, n):
    """
    Two-pass solution (length-based), with the off-by-one fixed.

    1) Count total nodes.
    2) Compute steps = length - n.
    3) Advance to the node *before* the one to delete.
    4) Bypass it.
    """
    dummy = ListNode(0, head)
    length = 0
    curr = head
    while curr:
        length += 1
        curr = curr.next

    # Step count to reach the node before the one to remove
    steps = length - n
    curr = dummy
    for _ in range(steps):
        curr = curr.next

    # Delete the nth-from-end node
    curr.next = curr.next.next
    return dummy.next

def remove_nth_last_node_two_pointer(head, n):
    """
    One-pass solution using two pointers.

    1) Move `first` pointer n+1 steps ahead.
    2) Move both `first` and `second` until `first` hits the end.
    3) `second.next` is the node to delete; bypass it.
    """
    dummy = ListNode(0, head)
    first = dummy
    second = dummy

    # Advance first n+1 steps ahead
    for _ in range(n + 1):
        first = first.next

    # Move both until first reaches the end
    while first:
        first = first.next
        second = second.next

    # Delete the target node
    second.next = second.next.next
    return dummy.next

def main():
    if len(sys.argv) != 3:
        print("Usage: python remove_nth_last_node.py \"[1,2,3,4,5]\" n")
        sys.exit(1)

    try:
        arr = ast.literal_eval(sys.argv[1])
        n = int(sys.argv[2])
    except Exception:
        print("Error: first argument must be a list of ints, second argument an integer")
        sys.exit(1)

    head = build_list(arr)
    out1 = remove_nth_last_node_length(head, n)

    head = build_list(arr)  # rebuild original list for the second test
    out2 = remove_nth_last_node_two_pointer(head, n)

    print("Input List:                    ", arr)
    print("After length-based removal:    ", list_to_pylist(out1))
    print("After two-pointer removal:     ", list_to_pylist(out2))

if __name__ == "__main__":
    main()

#  TC = O(N)
#  SC = O(1)
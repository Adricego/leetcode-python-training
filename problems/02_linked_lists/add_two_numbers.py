"""
Problem: Add Two Numbers
Difficulty: Medium
Topic: Linked List, Math

Summary:
Eng:
Two non-empty linked lists represent two non-negative integers.
The digits are stored in reverse order, and each node contains a single digit.
The task is to add both numbers and return the result as a linked list.
Esp:
Dos listas enlazadas no vacías representan dos enteros no negativos.
Los dígitos se almacenan en orden inverso, y cada nodo contiene un single dígito.
La tarea es sumar ambos números y devolver el resultado como una lista enlazada.

Important:
- The digits are stored in reverse order.
- Each node contains only one digit.
- The result must also be returned as a linked list.
- We should not convert the whole linked list into an integer, because the
goal is to practice linked list traversal and carry handling.

Example:
l1 = [2, 4, 3]
l2 = [5, 6, 4]

These represent:
342 + 465 = 807

Output:
[7, 0, 8]

Approach:
We traverse both linked lists at the same time, adding the values node by node.
At each step:
1. Get the current value from l1, or 0 if l1 is finished.
2. Get the current value from l2, or 0 if l2 is finished.
3. Add both values plus the carry.
4. The new digit is total % 10.
5. The new carry is total // 10.
6. Create a new node with the resulting digit.
7. Move to the next nodes.

A dummy head node is used to simplify the creation of the result linked list.

Complexity:
Time: O(max(n, m))
Space: O(max(n, m))

Where:
n = length of l1
m = length of l2
"""

from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self,
        l1: Optional[ListNode],
        l2: Optional[ListNode],
    ) -> Optional[ListNode]:
        dummy_head = ListNode(0)
        current = dummy_head
        carry = 0

        while l1 or l2 or carry:
            value1 = l1.val if l1 else 0
            value2 = l2.val if l2 else 0

            total = value1 + value2 + carry
            carry = total // 10
            digit = total % 10

            current.next = ListNode(digit)
            current = current.next

            if l1:
                l1 = l1.next

            if l2:
                l2 = l2.next

        return dummy_head.next


def list_to_linked_list(values: list[int]) -> Optional[ListNode]:
    dummy_head = ListNode(0)
    current = dummy_head

    for value in values:
        current.next = ListNode(value)
        current = current.next

    return dummy_head.next


def linked_list_to_list(head: Optional[ListNode]) -> list[int]:
    values = []

    while head:
        values.append(head.val)
        head = head.next

    return values


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        {
            "l1": [2, 4, 3],
            "l2": [5, 6, 4],
            "expected": [7, 0, 8],
        },
        {
            "l1": [0],
            "l2": [0],
            "expected": [0],
        },
        {
            "l1": [9, 9, 9, 9, 9, 9, 9],
            "l2": [9, 9, 9, 9],
            "expected": [8, 9, 9, 9, 0, 0, 0, 1],
        },
    ]

    for test in test_cases:
        l1 = list_to_linked_list(test["l1"])
        l2 = list_to_linked_list(test["l2"])

        result_head = solution.addTwoNumbers(l1, l2)
        result = linked_list_to_list(result_head)

        print("l1:", test["l1"])
        print("l2:", test["l2"])
        print("Expected:", test["expected"])
        print("Result:", result)
        print("Passed:", result == test["expected"])
        print("-" * 40)
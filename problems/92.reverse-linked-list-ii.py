#
# @lc app=leetcode id=92 lang=python3
#
# [92] Reverse Linked List II
#


# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


class Solution:
    def reverseBetween(
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:
        l: list[int] = []
        node = head

        while node:
            l.append(node.val)
            node = node.next

        reversed = l[left - 1 : right]
        reversed.reverse()

        l2: list[int] = l[: left - 1] + reversed + l[right:]

        root = node2 = ListNode()

        for element in l2:
            node2.next = ListNode(element)
            node2 = node2.next

        return root.next


# @lc code=end

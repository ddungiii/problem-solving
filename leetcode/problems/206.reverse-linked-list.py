#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#


# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(
            node: Optional[ListNode], prev: Optional[ListNode] = None
        ) -> Optional[ListNode]:
            if not node:
                return prev

            next, node.next = node.next, prev
            return reverse(next, node)

        return reverse(head)


# @lc code=end

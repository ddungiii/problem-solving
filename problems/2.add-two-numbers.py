#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#


# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        head = l1
        carry = 0
        while l1:
            val1 = l1.val
            val2 = l2.val if l2 else 0
            carry, val3 = divmod(val1 + val2 + carry, 10)
            l1.val = val3

            if l1.next is None:
                if carry:
                    l1.next = ListNode(carry)
                    break

            l1 = l1.next
            l2 = l2.next if l2 else None

        return head


# @lc code=end

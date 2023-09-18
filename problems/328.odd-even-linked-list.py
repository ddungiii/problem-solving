#
# @lc app=leetcode id=328 lang=python3
#
# [328] Odd Even Linked List
#


# @lc code=start
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        odd_root = odd = ListNode()
        even_root = even = ListNode()

        is_odd = True
        while head:
            if is_odd:
                odd.next = ListNode(head.val)
                odd = odd.next
            else:
                even.next = ListNode(head.val)
                even = even.next

            head = head.next
            is_odd = not is_odd

        odd.next = even_root.next

        return odd_root.next


# @lc code=end

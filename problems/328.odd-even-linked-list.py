#
# @lc app=leetcode id=328 lang=python3
#
# [328] Odd Even Linked List
#


# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def _is_even(val: int) -> bool:
            return val % 2 == 0

        if not head:
            return None

        head.next = self.oddEvenList(head.next)
        if head.next and _is_even(head.val) and not _is_even(head.next.val):
            next = head.next
            head.next, next.next = next.next, head
            head = next

            head.next = self.oddEvenList(head.next)

        return head


# @lc code=end

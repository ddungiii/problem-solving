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


from enum import Enum
from typing import Optional


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        class Type(Enum):
            ODD = 1
            EVEN = 2

        def _get_type(val: int) -> Type:
            return Type.EVEN if val % 2 == 0 else Type.ODD

        if not head:
            return None
        root_type = _get_type(head.val)

        def _is_root_type(val: int) -> bool:
            return _get_type(val) == root_type

        def _odd_even_list(head: Optional[ListNode]) -> Optional[ListNode]:
            if not head:
                return None

            head.next = _odd_even_list(head.next)

            if (
                head.next
                and not _is_root_type(head.val)
                and _is_root_type(head.next.val)
            ):
                next = head.next
                head.next, next.next = next.next, head
                head = next

                head.next = _odd_even_list(head.next)

            return head

        return _odd_even_list(head)


# @lc code=end

#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#


# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head and head.next:
            node = head.next
            head.next = self.swapPairs(node.next)
            node.next = head
            return node

        return head


# @lc code=end

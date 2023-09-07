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
        if not head:
            return None

        list = []
        while head:
            list.append(head.val)
            head = head.next
        list.reverse()

        head_reversed = node = ListNode(list[0])
        for i in range(1, len(list)):
            n = ListNode(list[i])
            node.next, node = n, n

        return head_reversed


# @lc code=end

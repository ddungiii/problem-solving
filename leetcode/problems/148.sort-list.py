#
# @lc app=leetcode id=148 lang=python3
#
# [148] Sort List
#


# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def get_length(self, head):
        node = head
        length = 0

        while node:
            node = node.next
            length += 1

        return length

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        length = self.get_length(head)
        left = head
        right = head
        for _ in range(int(length / 2)):
            right = right.next

        new = ListNode()
        while left or right:
            if not left:



# @lc code=end

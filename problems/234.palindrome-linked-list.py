#
# @lc app=leetcode id=234 lang=python3
#
# [234] Palindrome Linked List
#


# @lc code=start
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return True

        length = 0
        _head = head
        while _head:
            length += 1
            _head = _head.next

        stack = []
        for _ in range(int(length / 2)):
            stack.append(head.val)
            head = head.next

        if length % 2 == 1:
            head = head.next

        for _ in range(int(length / 2)):
            val = stack.pop()
            if val != head.val:
                return False
            head = head.next

        return True


# @lc code=end

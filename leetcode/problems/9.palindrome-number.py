#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#


# @lc code=start
import collections


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        queue = collections.deque(list(str(x)))
        while len(queue) > 1:
            if queue.popleft() != queue.pop():
                return False

        return True


# @lc code=end

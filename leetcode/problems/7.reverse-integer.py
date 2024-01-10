#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#


# @lc code=start
import ast
import collections


class Solution:
    def reverse(self, x: int) -> int:
        MAX_INT = 2**31 - 1
        MIN_INT = -(2**31)

        # 0. Preprocessing
        x_str = str(x)
        if len(x_str) == 1:
            return x

        sign = "+"
        if x_str[0] == "-":
            sign = "-"
            x_str = x_str[1:]

        # 1. Reverse
        l = collections.deque(list(x_str))
        l.reverse()

        # pruning
        pruning = 0
        for s in l:
            if s == "0":
                pruning += 1
            else:
                break

        for _ in range(pruning):
            l.popleft()

        x_reverse_str = "".join(l)
        x_reversed = ast.literal_eval(sign + x_reverse_str)

        if x_reversed > MAX_INT:
            return 0

        if x_reversed < MIN_INT:
            return 0

        return ast.literal_eval(sign + x_reverse_str)


# @lc code=end

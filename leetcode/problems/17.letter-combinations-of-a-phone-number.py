#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []

        digit_to_letter = {
            2: ["a", "b", "c"],
            3: ["d", "e", "f"],
            4: ["g", "h", "i"],
            5: ["j", "k", "l"],
            6: ["m", "n", "o"],
            7: ["p", "q", "r", "s"],
            8: ["t", "u", "v"],
            9: ["w", "x", "y", "z"],
        }

        letters: List[List[str]] = [digit_to_letter[int(digit)] for digit in digits]
        result = [""]

        def dfs(i):
            if i > len(letters) - 1:
                return

            for _ in range(len(result)):
                l = result.pop(0)
                for l2 in letters[i]:
                    new_l = l + l2
                    result.append(new_l)

            dfs(i + 1)

        dfs(0)

        return result


# @lc code=end

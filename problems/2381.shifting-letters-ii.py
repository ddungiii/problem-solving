#
# @lc app=leetcode id=2381 lang=python3
#
# [2381] Shifting Letters II
#


# @lc code=start
class Solution:
    def shiftingLetters(self, s: str, shifts: list[list[int]]) -> str:
        def _shiftChar(c: str, n: int) -> str:
            """
            a: 97, z: 122
            """
            new_ascii = ord(c) + n

            while new_ascii < 97:
                new_ascii += 26
            while new_ascii > 122:
                new_ascii -= 26

            return chr(new_ascii)

        indexes = [0 for _ in range(len(s))]
        result = ""

        for shift in shifts:
            direction = 1 if shift[2] == 1 else -1
            for i in range(shift[0], shift[1] + 1):
                indexes[i] += direction

        for i, index in enumerate(indexes):
            result += _shiftChar(s[i], index)

        return result


# @lc code=end

import time

solution = Solution()
shifts = []
s = input("s: ")
n = int(input("n: "))
for _ in range(n):
    input_string = input("")
    input_list = input_string.split()
    shifts.append([int(str) for str in input_list])


start = time.time()
print(solution.shiftingLetters(s, shifts))
print(f"time: {time.time() - start:.4f}s")

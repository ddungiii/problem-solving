#
# @lc app=leetcode id=461 lang=python3
#
# [461] Hamming Distance
#


# @lc code=start
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        def count_bits(number):
            cnt = 0
            while number > 0:
                if number % 2 == 1:
                    cnt += 1

                number = number >> 1

            return cnt

        return count_bits(x ^ y)


# @lc code=end

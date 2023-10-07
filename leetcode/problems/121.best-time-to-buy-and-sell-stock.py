#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#


# @lc code=start
import sys


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if len(prices) == 0:
            return 0

        buy_price = sys.maxsize
        profit = 0

        for price in prices:
            buy_price = min(price, buy_price)
            profit = max(profit, price - buy_price)

        return profit


# @lc code=end

import time

soluion = Solution()
start = time.time()
input_string = input("_: ")
input_list = input_string.split()
input = [int(str) for str in input_list]
print(soluion.maxProfit(input))
print(f"time: {time.time() - start:.4f}s ")

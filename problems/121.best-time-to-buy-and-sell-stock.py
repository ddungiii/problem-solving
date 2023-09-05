#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#


# @lc code=start
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if len(prices) == 0:
            return 0

        buy, sell, profit = 0, 0, 0

        for i in range(1, len(prices)):
            buy_price = prices[buy]
            sell_price = prices[sell]
            current_price = prices[i]

            if buy_price > current_price:
                buy, sell, profit = i, i, 0
                continue

            current_profit = current_price - buy_price
            if current_profit > profit:
                profit = current_profit

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

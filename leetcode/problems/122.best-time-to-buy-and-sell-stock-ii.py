#
# @lc app=leetcode id=122 lang=python3
#
# [122] Best Time to Buy and Sell Stock II
#


# @lc code=start
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit = 0
        cur = prices[0]

        for price in prices:
            if price < cur:
                cur = price
            elif price > cur:
                profit += price - cur
                cur = price

        return profit


# @lc code=end

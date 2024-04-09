#
# @lc app=leetcode id=134 lang=python3
#
# [134] Gas Station
#


# @lc code=start
class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        def travel(start):
            index = start
            walk = 0

            tank = 0
            while walk < N:
                tank += gas[index]
                tank -= cost[index]

                if tank < 0:
                    return -1

                index += 1
                index %= N
                walk += 1

            return start

        N = len(gas)

        for start in range(N):
            result = travel(start)
            if result >= 0:
                return result

        return -1


# @lc code=end

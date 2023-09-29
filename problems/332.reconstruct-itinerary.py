#
# @lc app=leetcode id=332 lang=python3
#
# [332] Reconstruct Itinerary
#
from collections import defaultdict
from pickletools import stackslice
from typing import List
# @lc code=start
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)

        for key, value in sorted(tickets):
            graph[key].append(value)

        route, stack = [], ['JFK']
        while stack:
            while graph[stack[-1]]:
                stack.append(graph[stack[-1]].pop(0))
            route.append(stack.pop())

        return route[::-1]

            

        
# @lc code=end


#
# @lc app=leetcode id=332 lang=python3
#
# [332] Reconstruct Itinerary
#
from collections import defaultdict
from typing import List
# @lc code=start
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)

        for key, value in sorted(tickets, reverse=True):
            graph[key].append(value)

        def dfs(node: str):
            while graph[node]:
                dfs(graph[node].pop())
            route.append(node)

        route =[]
        dfs('JFK')
        return route[::-1]

            

        
# @lc code=end


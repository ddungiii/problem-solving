#
# @lc app=leetcode id=332 lang=python3
#
# [332] Reconstruct Itinerary
#
from typing import List
# @lc code=start
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort(key=lambda ticket: [ticket[0], ticket[1]])

        def dfs(tickets: List[List[str]], itinerary: List[str]):
            if not len(tickets):
                return itinerary
            
            last = itinerary[-1]
            
            for i, ticket in enumerate(tickets):
                if ticket[0] == last:
                    new_tickets = tickets[:]
                    new_tickets.pop(i)
                    result = dfs(new_tickets, itinerary + [ticket[1]])
                    if result:
                        return result
        
        
        return dfs(tickets, ["JFK"])

        
# @lc code=end


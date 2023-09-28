#
# @lc app=leetcode id=332 lang=python3
#
# [332] Reconstruct Itinerary
#
from imp import init_frozen
from socket import TIPC_HIGH_IMPORTANCE
from typing import List
# @lc code=start
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort(key=lambda ticket: (ticket[0], ticket[1]))

        def dfs(index: int, tickets: List[List[str]], itinerary: List[str]):
            if not len(tickets):
                return itinerary
            
            last = itinerary[-1]
            
            result=itinerary
            for i, ticket in enumerate(tickets):
                if ticket[0] == last:
                    new_tickets = tickets[:]
                    new_tickets.remove(ticket)
                    result = dfs(i+1, new_tickets, itinerary + [ticket[1]])

            return result
        
        
        return dfs(0, tickets, ["JFK"])

        
# @lc code=end


#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#
from collections import defaultdict
from typing import List
from xmlrpc.client import getparser
# @lc code=start
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not len(prerequisites):
            return True
        
        graph = defaultdict(list)
        for a, b in prerequisites:
            graph[a].append(b)

        def dfs(i: int):
            if i in trace:
                return False
            
            trace.add(i)
            for x in graph[i]:
                if not dfs(x):
                    return False
            trace.remove(i)

            return True

        trace = set()

        for x in list(graph):
            if not dfs(x):
                return False
            
        return True
        
# @lc code=end


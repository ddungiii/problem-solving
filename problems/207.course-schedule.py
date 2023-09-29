#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#
from typing import List
from xmlrpc.client import getparser
# @lc code=start
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # If a Circular Dependency Exists, Fail to finish courses
        if not len(prerequisites):
            return True
        
        graph = dict()
        for a, b in prerequisites:
            graph[a] = b

        result = True
        def dfs(course: int):
            print(course, graph, route)
            if course in graph:
                if graph[course] in route:
                    return False

                route.append(course)
                print(route)
                return dfs(graph.pop(course))
            
            return True
        
        route = []
        
        return dfs(prerequisites[0][0])
        
# @lc code=end


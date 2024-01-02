#
# @lc app=leetcode id=743 lang=python3
#
# [743] Network Delay Time
#


# @lc code=start
import ast
import collections
import heapq
from typing import List


class Solution:
    def dijkstra(self, graph, start):
        dist = collections.defaultdict(int)
        Q = [(start, 0)]

        while Q:
            node, weight = heapq.heappop(Q)
            if node not in dist:
                dist[node] = weight
                for v, w in graph[node]:
                    alt = w + weight
                    heapq.heappush(Q, (v, alt))

        return dist

    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        dist = self.dijkstra(graph, k)
        print(dist)
        if len(dist) == n:
            return max(dist.values())

        return -1


# @lc code=end
import time

soluion = Solution()
start = time.time()

times = ast.literal_eval(input("times: "))
times = [[int(element) for element in sublist] for sublist in times]
n = int(input("n: "))
k = int(input("k: "))


print(soluion.networkDelayTime(times, n, k))
print(f"time: {time.time() - start:.4f}s ")

#
# @lc app=leetcode id=787 lang=python3
#
# [787] Cheapest Flights Within K Stops
#
import collections
import heapq
from typing import List


# @lc code=start
class Solution:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        graph = collections.defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))

        Q = [(0, src, 0)]  # weight, node, depth

        while Q:
            weight, node, depth = heapq.heappop(Q)
            if node == dst:
                return weight

            if depth <= k:
                for v, w in graph[node]:
                    alt = w + weight
                    heapq.heappush(Q, (alt, v, depth + 1))

        return -1


# @lc code=end
import ast
import time

soluion = Solution()
start = time.time()

n = int(input("n: "))
flights = ast.literal_eval(input("flights: "))
flights = [[int(e) for e in l] for l in flights]
src = int(input("src: "))
dst = int(input("dst: "))
k = int(input("k: "))

print(soluion.findCheapestPrice(n, flights, src, dst, k))
print(f"time: {time.time() - start:.4f}s ")

#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#
from dis import disco
from typing import List

# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0])
        print(f"n: {n}, m: {m}")
        
        class Point:
            def __init__(self, x, y) -> None:
                self.x = x
                self.y = y 

        def get_neighbors(point: Point):
            x, y = point.x, point.y

            xs, ys = [x, x+1] if x < n-1 else [x], [y, y+1] if y < m-1 else [y]

            neighbors = []
            for new_x in xs:
                for new_y in ys:
                    neighbors.append(Point(new_x, new_y))


            return neighbors

        
        discoverd = [[0 for _ in range(m)] for _ in range(n)]
        
        def dfs(num_islands: int, point: Point = Point(0, 0)):
            x, y = point.x, point.y
            discoverd[x][y] = 1

            if grid[x][y] == "1" and (x > 0 and grid[x-1][y] == "0") and (y > 0 and grid[x][y-1] == "0"):
                print("new!")
                num_islands += 1

            print(f"grid[{x}][{y}]: {grid[x][y]} nums: {num_islands}")
            neighbors = get_neighbors(point)
            for neighbor in neighbors:
                print(f"new_x: {neighbor.x}, new_y: {neighbor.y}")
                if discoverd[neighbor.x][neighbor.y] == 0:
                    num_islands = max(num_islands, dfs(num_islands, neighbor))

            return num_islands   
        
        num_islands = dfs(1) 

        return num_islands
        
# @lc code=end

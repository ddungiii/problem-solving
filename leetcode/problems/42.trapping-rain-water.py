#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#


# @lc code=start


class Solution:
    def trap(self, height: list[int]) -> int:
        stack = []
        volume = 0

        for i in range(len(height)):
            while stack and height[i] > height[stack[-1]]:
                top = stack.pop()
                if not len(stack):
                    break

                distance = i - stack[-1] - 1
                water = min(height[i], height[stack[-1]]) - height[top]

                volume += distance * water

            stack.append(i)

        return volume


# @lc code=end
import time

soluion = Solution()
start = time.time()
height_string = input("height: ")
height_list = height_string.split()
heights = [int(h) for h in height_list]
print(soluion.trap(heights))
print(f"time: {time.time() - start:.4f}s ")

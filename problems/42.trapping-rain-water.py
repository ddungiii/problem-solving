#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#


# @lc code=start


class Solution:
    def trap(self, height: list[int]) -> int:
        total = 0
        len_heights = len(height)
        top_index = height.index(max(height))
        reversed_height = height[::-1]

        def find_trapped_water(height: list[int], left: int) -> tuple[int, int]:
            right = left + 1
            for _ in range(len_heights - left):
                if right >= len_heights or height[left] <= height[right]:
                    break

                right += 1
            m = min(height[left], height[right])

            trapped = [m - h for h in height[left + 1 : right]]

            return right, sum(trapped)

        # find trapped water from left
        left = 0
        while 1:
            if left >= top_index - 1:
                break
            left, trapped = find_trapped_water(height, left)

            total += trapped

        # find trapped water from right
        right = 0
        while 1:
            if right >= len_heights - top_index - 1:
                break
            right, trapped = find_trapped_water(reversed_height, right)

            total += trapped

        return total


# @lc code=end
import time

soluion = Solution()
start = time.time()
height_string = input("height: ")
height_list = height_string.split()
heights = [int(h) for h in height_list]
print(soluion.trap(heights))
print(f"time: {time.time() - start:.4f}s ")

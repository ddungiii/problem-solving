#
# @lc app=leetcode id=621 lang=python3
#
# [621] Task Scheduler
#


# @lc code=start
import collections
import heapq


class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        counter = collections.Counter(tasks)
        result = 0

        while True:
            _result = 0

            for task, _ in counter.most_common(n + 1):
                result += 1
                _result += 1

                # Remove task in counter
                counter.subtract(task)
                # Remove task counts under 0
                counter += collections.Counter()

            if not counter:
                break

            result += n - _result + 1

        return result


# ["D", "B","B","B","A","C","A"]\n2

# @lc code=end

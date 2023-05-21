#
# @lc app=leetcode id=937 lang=python3
#
# [937] Reorder Data in Log Files
#

# @lc code=start


class Solution:
    def reorderLogFiles(self, logs: list[str]) -> list[str]:
        letters = []
        digits = []

        for log in logs:
            if log.split()[1].isalpha():
                letters.append(log)
            else:
                digits.append(log)

        letters.sort(key=lambda log: (log.split()[1:], log.split()[0]))

        return letters + digits


# @lc code=end

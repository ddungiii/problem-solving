#
# @lc app=leetcode id=937 lang=python3
#
# [937] Reorder Data in Log Files
#

# @lc code=start


class Solution:
    def reorderLogFiles(self, logs: list[str]) -> list[str]:
        logs.sort(
            key=lambda s: (
                -s.split()[1].isalpha(),
                s.split()[1] if s.split()[1].isalpha() else 0,
            )
        )

        # logs.sort(key=lambda s: s.split()[1])
        return logs


# @lc code=end

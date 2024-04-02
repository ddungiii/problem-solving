#
# @lc app=leetcode id=393 lang=python3
#
# [393] UTF-8 Validation
#


# @lc code=start
class Solution:
    def validUtf8(self, data: list[int]) -> bool:
        def get_bytes(b):
            for i, s in enumerate(start):
                if b[: len(s)] == s:
                    return 4 - i

            return -1

        start = ["11110", "1110", "110", "0", "10"]
        data = [bin(d)[2:].zfill(8) for d in data]

        i = 0
        while i < len(data):
            bytes = get_bytes(data[i])
            if bytes <= 0:
                # following byte or invalid
                return False

            for _ in range(bytes - 1):
                i += 1
                if i >= len(data) or get_bytes(data[i]) != 0:
                    return False

            i += 1

        return True


# @lc code=end

def squash(s, n):
    squashed = ""

    i = 0
    while i < len(s):
        cur = s[i : i + n]
        count = 1
        j = i + n
        while j < len(s):
            next = s[j : j + n]
            if cur == next:
                count += 1
            else:
                break
            j += n

        count = count if count > 1 else ""
        squashed += f"{count}{cur}"
        i = j

    return squashed


def solution(s):
    min_len = len(s)
    for i in range(1, len(s) // 2 + 1):
        squashed = squash(s, i)
        min_len = min(min_len, len(squashed))

    return min_len

def dfs(q1, q2, count):
    if count == len(q1) + len(q2):
        return count

    if len(q1) == 0 or len(q1) == 0:
        return -1

    return min(
        dfs([q2[0]] + q1, q2[1:], count + 1),
        dfs(q1[1:], [q1[0]] + q2, count + 1),
    )


def solution(queue1, queue2):
    # 1. If sum is odd, FAIL
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    if (sum1 + sum2) % 2 != 0:
        return -1

    # 2. DFS? (BRUTE FORCE?)
    return dfs(queue1, queue2, 0)


print(
    solution(
        [
            3,
            2,
            7,
            2,
        ],
        [4, 6, 5, 1],
    )
)

print(solution([1, 2, 1, 2], [1, 10, 1, 2]))

print(solution([1, 1], [1, 5]))

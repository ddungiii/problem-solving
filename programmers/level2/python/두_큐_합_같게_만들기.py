import collections


def solution(queue1, queue2):
    q1 = collections.deque(queue1)
    q2 = collections.deque(queue2)
    s1, s2 = sum(q1), sum(q2)

    if (s1 + s2) % 2 != 0:
        return -1

    count = 0
    max_count = s1 * 3  # why?
    while count < max_count:
        if s1 == s2:
            return count

        elif s1 > s2:
            q2.append(q1.popleft())

        elif s2 > s1:
            q1.append(q2.popleft())

        s1 = sum(q1)
        s2 = sum(q2)
        count += 1

    return -1


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

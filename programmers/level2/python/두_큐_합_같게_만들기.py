import collections


def solution(queue1, queue2):
    q1 = collections.deque(queue1)
    q2 = collections.deque(queue2)
    s1, s2 = sum(q1), sum(q2)

    if (s1 + s2) % 2 != 0:
        return -1

    count = 0
    # Why len(q1) * 3 require?
    # Because q2+q1, q1+q2 is different
    #
    # 1. len(q1) : q1: -, q2: q2+q1
    # 2. len(q1) : q1: q2, q2: q1 (return)
    # 3. len(q1) : q1: q2+q1, q2: -
    #
    # => 1+2+3 = len(q1) * 3
    max_count = len(q1) * 3
    while count < max_count:
        if s1 == s2:
            return count

        elif s1 > s2:
            e = q1.popleft()
            q2.append(e)
            s1 -= e
            s2 += e

        elif s2 > s1:
            e = q2.popleft()
            q1.append(e)
            s2 -= e
            s1 += e

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

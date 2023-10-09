"""
https://www.acmicpc.net/problem/17471

6
5 2 3 4 1 2
2 2 4
4 1 3 6 5
2 4 2
2 1 3
1 2
1 2
"""
from itertools import permutations


def calc_diff():
    sum_a = sum([population[a] for a in A])
    sum_b = sum([population[b] for b in B])

    return abs(sum_a - sum_b)


def dfs(a, b):
    if a == b:
        return float("inf")
    # print(f"dfs {a} {b}")
    # print(A)
    # print(B)

    if len(A) + len(B) == N:
        # print("found")
        # print(A)
        # print(B)
        # print(calc_diff())
        return calc_diff()

    neighbors_a = neighbors[a]
    neighbors_b = neighbors[b]

    diffs = []
    for neighbor_a in neighbors_a:
        for neighbor_b in neighbors_b:
            if not neighbor_a in A and not neighbor_a in B:
                A.append(neighbor_a)
                diffs.append(dfs(neighbor_a, b))
                A.pop()

                if not neighbor_b in B and not neighbor_b in A:
                    B.append(neighbor_b)
                    diffs.append(dfs(a, neighbor_b))

                    A.append(neighbor_a)
                    diffs.append(dfs(neighbor_a, neighbor_b))
                    A.pop()
                    B.pop()

    return min(diffs) if diffs else float("inf")


def solution():
    """
    dfs, backtracking

    until len(A)+len(B) == N

    Where is starting point A, B?
    """
    answer = float("inf")
    for perm in permutations(range(N), 2):
        a, b = perm

        A.append(a)
        B.append(b)
        diff = dfs(a, b)
        A.pop()
        B.pop()
        answer = min(answer, diff)

    return answer


N = int(input())
population = list(map(int, input().split()))
neighbors = []
for i in range(N):
    neighbor = list(map(int, input().split()[1:]))
    neighbor = [n - 1 for n in neighbor]
    neighbors.append(neighbor)

A, B = [], []
print(solution())

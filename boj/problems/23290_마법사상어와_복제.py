"""
https://www.acmicpc.net/problem/23290

input:
5 1
4 3 5
1 3 5
2 4 2
2 1 6
3 4 4
4 2

output:
9
"""

import collections


M, S = map(int, input().split())
fishes = collections.defaultdict(list)
for _ in range(M):
    r, c, d = map(int, input().split())
    fishes[(r, c)].append(d)

shark = tuple(map(int, input().split()))

"""
X, ←, ↖, ↑, ↗, →, ↘, ↓, ↙
Ignore index 0
"""
dr = (0, 0, -1, -1, -1, 0, 1, 1, 1)
dc = (0, -1, -1, 0, 1, 1, 1, 0, -1)

"""
↑, ←, ↓, →
"""
dr_shark = (-1, 0, 1, 0)
dc_shark = (0, -1, 0, 1)


def magic_start(fishes: collections.defaultdict):
    """
    1.
    상어가 모든 물고기에게 복제 마법을 시전한다.
    복제 마법은 시간이 조금 걸리기 때문에, 아래 5번에서 물고기가 복제되어 칸에 나타난다.
    """
    return list(fishes.items())[:]


def get_next_fish(fish: tuple) -> tuple:
    r, c, d = fish

    change = False
    for _ in range(8):
        next_r, next_c = r + dr[d], c + dc[d]
        if (
            1 <= next_r < 5
            and 1 <= next_c < 5
            and (next_r, next_c) != shark
            and (next_r, next_c) not in old_blood
            and (next_r, next_c) not in blood
        ):
            change = True
            break
        d -= 1
        d %= 9
        if d == 0:
            d = 8

    return (next_r, next_c, d) if change else (r, c, d)


def move_fishes(fishes: collections.defaultdict):
    """
    2.
    모든 물고기가 한 칸 이동한다.
    상어가 있는 칸, 물고기의 냄새가 있는 칸, 격자의 범위를 벗어나는 칸으로는 이동할 수 없다.
    각 물고기는 자신이 가지고 있는 이동 방향이 이동할 수 있는 칸을 향할 때까지 방향을 45도 반시계 회전시킨다.
    만약, 이동할 수 있는 칸이 없으면 이동을 하지 않는다. 그 외의 경우에는 그 칸으로 이동을 한다.
    물고기의 냄새는 아래 3에서 설명한다.
    """
    next_fishes = []
    for r, c in list(fishes):
        directions = fishes.pop((r, c))
        for direction in directions:
            next_fishes.append(get_next_fish((r, c, direction)))

    for r, c, d in next_fishes:
        fishes[(r, c)].append(d)


def get_repetitive_permutations(n, k):
    result = []

    for i in range(n):
        for j in range(n):
            for k in range(n):
                result.append((i, j, k))

    return result


def move_shark(shark):
    """
    3.
    상어가 연속해서 3칸 이동한다. 상어는 현재 칸에서 상하좌우로 인접한 칸으로 이동할 수 있다.
    연속해서 이동하는 칸 중에 격자의 범위를 벗어나는 칸이 있으면, 그 방법은 불가능한 이동 방법이다.
    연속해서 이동하는 중에 상어가 물고기가 있는 같은 칸으로 이동하게 된다면,
    그 칸에 있는 모든 물고기는 격자에서 제외되며, 제외되는 모든 물고기는 물고기 냄새를 남긴다.
    가능한 이동 방법 중에서 제외되는 물고기의 수가 가장 많은 방법으로 이동하며,
    그러한 방법이 여러가지인 경우 사전 순으로 가장 앞서는 방법을 이용한다. 사전 순에 대한 문제의 하단 노트에 있다.

    4.
    두 번 전 연습에서 생긴 물고기의 냄새가 격자에서 사라진다.
    """

    def _check(perm):
        blooded = 0
        nr, nc = shark
        visited = set()

        for i in perm:
            nr = nr + dr_shark[i]
            nc = nc + dc_shark[i]

            if 1 <= nr < 5 and 1 <= nc < 5 and (nr, nc) not in visited:
                fish = fishes[(nr, nc)]
                blooded += len(fish)
                visited.add((nr, nc))
            else:
                return -1

        return blooded

    perms = get_repetitive_permutations(4, 3)
    count = 0
    route = (-1, -1, -1)

    for perm in perms:
        new_count = _check(perm)
        if new_count > count or (new_count >= 0 and route[0] < 0):
            count = new_count
            route = perm

    nr, nc = shark
    blood = []
    for r in route:
        nr, nc = nr + dr_shark[r], nc + dc_shark[r]

        poped = fishes.pop((nr, nc))
        if len(poped) > 0:
            blood.append((nr, nc))

    return (nr, nc), blood


def magic_finish(replicated_fishes):
    """
    5.
    1에서 사용한 복제 마법이 완료된다. 모든 복제된 물고기는 1에서의 위치와 방향을 그대로 갖게 된다.
    """
    for fish, directions in replicated_fishes:
        for direction in directions:
            fishes[fish].append(direction)


old_blood = []
blood = []
for _ in range(S):
    replicated_fishes = magic_start(fishes)
    move_fishes(fishes)
    shark, new_blood = move_shark(shark)
    old_blood, blood = blood, new_blood
    magic_finish(replicated_fishes)

print(sum([len(fishes[fish]) for fish in list(fishes)]))

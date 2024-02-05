import collections
import copy
from re import M

DEBUG = True


def print_mat(mat):
    if not DEBUG:
        return

    for r in mat:
        for c in r:
            print(f"{c}\t", end=" ")
        print()
    print()


def expand(key, lock):
    """
    {key}가 move할 수 있는 거리만큼, {key}와 {lock} matrix들을 확장시킵니다.

    key는 (0,0)에, lock은 중심에 위치시킵니다.
    """
    empty_line = collections.deque([-1 for _ in range(2 * N - 2 + M)])

    new_key = collections.deque()
    for r in key:
        new_key.append(collections.deque(r + [-1 for _ in range(M - 2 + N)]))
    for _ in range(M - 2 + N):
        new_key.append(empty_line)

    print_mat(new_key)

    new_lock = collections.deque()
    for _ in range(N - 1):
        new_lock.append(empty_line)

    for r in lock:
        bump = [-1 for _ in range(N - 1)]
        new_lock.append(collections.deque(bump + r + bump))

    for _ in range(N - 1):
        new_lock.append(empty_line)

    print_mat(new_lock)

    return new_key, new_lock


def rotate(mat):
    """
    {mat}를 시계방향으로 회전시킨다.
    """

    new_mat = collections.deque([collections.deque() for _ in range(len(mat))])
    for row in mat:
        for i, e in enumerate(row):
            new_mat[i].appendleft(e)

    return new_mat


def move(key, dx, dy):
    """
    {mat}를 x방향으로 {dx}, y방향으로 {dy} 이동시킵니다.
    """
    moved = copy.deepcopy(key)
    for i in range(M):
        for _ in range(dx):
            moved[i].pop()
            moved[i].appendleft(-1)

    for _ in range(dy):
        moved.pop()
        moved.appendleft([-1 for _ in range(2 * N - 2 + M)])

    return moved


def get_key(key, value):
    """
    {key}의 돌기 position을 반환합니다.
    """
    l = len(key)
    keys = []
    for r in range(l):
        for c in range(l):
            if key[r][c] == value:
                keys.append((r, c))

    return keys


def is_key(key_keys, lock, lock_keys):
    cnt = 0
    for r, c in key_keys:
        if lock[r][c] == 1:
            return False
        elif lock[r][c] == 0:
            cnt += 1

    return cnt == len(lock_keys)


def solution(key, lock):
    global N
    global M
    N = len(key)
    M = len(lock)

    key, lock = expand(key, lock)

    for _ in range(4):
        if _ > 0:
            key = rotate(key)

        for x in range(M - 1 + N):
            for y in range(M - 1 + N):
                print(x, y)
                new_key = move(key, x, y)
                print_mat(new_key)
                key_keys = get_key(new_key, 1)
                lock_keys = get_key(lock, 0)
                if is_key(key_keys, lock, lock_keys):
                    return True

    return False


key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
print(solution(key, lock))

# 40분


def solution(cap, n, deliveries, pickups):
    distance = 0

    d = 0
    p = 0
    for i in range(n - 1, -1, -1):
        # 이번에 처리해야하는 양
        d += deliveries[i]
        p += pickups[i]

        while d > 0 or p > 0:
            distance += i + 1
            # cap만큼 처리함
            # 음수가 되면, 다음 차례에서 처리해야하는 양을 더할 때, 감안됨
            d -= cap
            p -= cap

    return distance * 2

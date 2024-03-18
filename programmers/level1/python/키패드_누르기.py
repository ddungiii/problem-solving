def calc_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def solution(numbers, hand):
    # 1. keypad to map
    pad = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ["*", 0, "#"]]
    num_positions = {}

    for i in range(4):
        for j in range(3):
            num_positions[pad[i][j]] = (i, j)

    left = (3, 0)
    right = (3, 2)

    # 2. for number, calc distance and move hand
    answer = ""
    left_pad = [1, 4, 7]
    right_pad = [3, 6, 9]
    for num in numbers:
        pos = num_positions[num]
        if num in left_pad:
            left = pos
            answer += "L"
            continue
        elif num in right_pad:
            right = pos
            answer += "R"
            continue

        left_distance = calc_distance(left, pos)
        right_distance = calc_distance(right, pos)

        if left_distance < right_distance:
            left = pos
            answer += "L"
        elif right_distance < left_distance:
            right = pos
            answer += "R"
        else:
            if hand == "right":
                right = pos
                answer += "R"
            else:
                left = pos
                answer += "L"

    return answer

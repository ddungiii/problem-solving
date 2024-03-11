import collections


def solution(survey, choices):
    dict = collections.defaultdict(int)

    # 1. Select
    for sur, choice in zip(survey, choices):
        print(sur, choice)
        direction = 1 if choice > 4 else 0
        point = 4 - choice if choice < 4 else choice - 4

        dict[sur[direction]] += point

    # 2. Get
    answer = ""
    types = ["RT", "CF", "JM", "AN"]  # sorted by ascending
    for type in types:
        first = dict[type[0]]
        second = dict[type[1]]

        if first >= second:
            answer += type[0]
        else:
            answer += type[1]

    return answer


# print(solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]))
# print(solution(["TR", "RT", "TR"], [7, 1, 3]))
# print(solution(["CF"], [1]))
# print(solution(["CF"], [2]))
# print(solution(["CF"], [3]))
# print(solution(["CF"], [4]))
# print(solution(["CF"], [5]))
# print(solution(["CF"], [6]))
# print(solution(["CF"], [7]))
# print(solution(["FC"], [4]))
print(solution(["FC", "FC"], [4, 1]))

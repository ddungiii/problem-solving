from bisect import bisect_left, insort_right


def binary_search(list, num):
    low = 0
    high = len(list)

    while low < high:
        mid = (low + high) // 2
        if num <= list[mid]:
            high = mid
        else:
            low = mid + 1

    return low


def solution(info, query):
    languages = ["java", "python", "cpp"]
    job = ["frontend", "backend"]
    year = ["junior", "senior"]
    food = ["pizza", "chicken"]

    # 1. Create Tree
    tree = [[[[[] for _ in food] for _ in year] for _ in job] for _ in languages]
    for applicant in info:
        l, j, y, f, point = applicant.split(" ")

        l_i = languages.index(l)
        j_i = job.index(j)
        y_i = year.index(y)
        f_i = food.index(f)

        insort_right(tree[l_i][j_i][y_i][f_i], int(point))

    # 2. Querying
    answer = []
    for q in query:
        l, j, y, food_point = [e.strip() for e in q.split("and")]
        f, point = food_point.split()

        l_indexes = [languages.index(l)] if l in languages else [0, 1, 2]
        j_indexes = [job.index(j)] if j in job else [0, 1]
        y_indexes = [year.index(y)] if y in year else [0, 1]
        f_indexes = [food.index(f)] if f in food else [0, 1]

        count = 0
        for l_i in l_indexes:
            for j_i in j_indexes:
                for y_i in y_indexes:
                    for f_i in f_indexes:
                        target = tree[l_i][j_i][y_i][f_i]
                        if not target:
                            continue
                        lowest_index = bisect_left(target, int(point))
                        count += len(target) - lowest_index

        answer.append(count)

    return answer


print(
    solution(
        [
            "java backend junior pizza 150",
            "python frontend senior chicken 210",
            "python frontend senior chicken 150",
            "python frontend senior chicken 302",
            "python frontend senior chicken 1",
            "python frontend senior chicken 5930",
            "cpp backend senior pizza 260",
            "java backend junior chicken 80",
            "python backend senior chicken 50",
        ],
        [
            "java and backend and junior and pizza 100",
            "python and frontend and senior and chicken 200",
            "python and frontend and senior and chicken 302",
            "cpp and - and senior and pizza 250",
            "- and backend and senior and - 150",
            "- and - and - and chicken 100",
            "- and - and - and - 150",
        ],
    )
)

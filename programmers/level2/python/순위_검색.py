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

        tree[l_i][j_i][y_i][f_i].append(int(point))

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

                        count += len(
                            [a for a in tree[l_i][j_i][y_i][f_i] if a >= int(point)]
                        )

        answer.append(count)

    return answer


print(
    solution(
        [
            "java backend junior pizza 150",
            "python frontend senior chicken 210",
            "python frontend senior chicken 150",
            "cpp backend senior pizza 260",
            "java backend junior chicken 80",
            "python backend senior chicken 50",
        ],
        [
            "java and backend and junior and pizza 100",
            "python and frontend and senior and chicken 200",
            "cpp and - and senior and pizza 250",
            "- and backend and senior and - 150",
            "- and - and - and chicken 100",
            "- and - and - and - 150",
        ],
    )
)

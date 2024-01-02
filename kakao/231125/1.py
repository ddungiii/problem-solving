"""
["muzi", "ryan", "frodo", "neo"]
["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"]


["joy", "brad", "alessandro", "conan", "david"]
["alessandro brad", "alessandro joy", "alessandro conan", "david alessandro", "alessandro david"]

["a", "b", "c"]
["a b", "b a", "c a", "a c", "a c", "c a"]
"""


def solution(friends, gifts):
    def get_index(friend):
        return friends.index(friend)

    # Pre-processing
    matrix = [[0 for _ in range(len(friends))] for _ in range(len(friends))]
    for gift in gifts:
        s, r = gift.split()
        matrix[get_index(s)][get_index(r)] += 1

    score = []
    for i in range(len(friends)):
        send = sum(matrix[i])
        receive = sum([row[i] for row in matrix])
        score.append(send - receive)

    # Predict next month gifts
    predict = [0 for _ in range(len(friends))]
    for r in range(len(friends)):
        for s in range(len(friends)):
            if r == s:
                continue

            sent = matrix[r][s]
            received = matrix[s][r]
            if sent > received:
                predict[r] += 1
            elif (sent == received) and (score[r] > score[s]):
                predict[r] += 1

    return max(predict)


friends = ["a", "b", "c"]
gifts = ["a b", "b a", "c a", "a c", "a c", "c a"]
print(solution(friends, gifts))

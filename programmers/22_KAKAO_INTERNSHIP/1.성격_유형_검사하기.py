def solution(survey, choices):
    def _evaluate(chars, choice):
        if choice < 4:
            score = 4 - choice
            scores[chars[0]] += score
        elif choice > 4:
            score = choice - 4
            scores[chars[1]] += score

    def _get_answer():
        answer = ""
        for l, r in types:
            l_score, r_score = scores[l], scores[r]

            if r_score > l_score:
                answer += r
            else:
                answer += l

        return answer

    types = [("R", "T"), ("C", "F"), ("J", "M"), ("A", "N")]
    scores = {}
    for l, r in types:
        scores[l] = 0
        scores[r] = 0

    for s, c in zip(survey, choices):
        _evaluate(s, c)

    print(scores)

    return _get_answer()


if __name__ == "__main__":
    print(solution(["TR", "RT", "TR"], [7, 1, 3]))

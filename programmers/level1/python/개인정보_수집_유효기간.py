def parse_date(date_str: str):
    return [int(d) for d in date_str.split(".")]


def parse_terms(terms):
    term_dict = {}
    for term in terms:
        type, month = term.split(" ")[0], term.split(" ")[1]
        term_dict[type] = int(month)
    return term_dict


def parse_privacies(privacies):
    result = []
    for privacy in privacies:
        privacy_list = privacy.split(" ")
        date, type = parse_date(privacy_list[0]), privacy_list[1]

        result.append((date, type))

    return result


def is_expired(privacy, terms, today):
    date, type = privacy
    date[1] += terms[type]
    while date[1] > 12:
        date[1] -= 12
        date[0] += 1

    for d, t in zip(date, today):
        if d > t:
            return False
        elif d < t:
            return True

    return True


def solution(today, terms, privacies):
    today = parse_date(today)
    terms = parse_terms(terms)
    privacies = parse_privacies(privacies)

    answer = []
    for i, privacy in enumerate(privacies):
        if is_expired(privacy, terms, today):
            answer.append(i + 1)

    return answer


print(
    solution(
        "2022.05.19",
        ["A 6", "B 12", "C 3"],
        ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"],
    )
)

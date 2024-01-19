def solution(n, words):
    used = []
    lastchar = words[0][0]

    who, turn = 0, 0

    for i, word in enumerate(words):
        if word[0] != lastchar or word in used:
            who = i % n + 1
            turn = int(i / n) + 1
            break

        used.append(word)
        lastchar = word[-1]

    return who, turn


print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]))

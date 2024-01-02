"""
4
[3, 6, 7, 2, 1, 10, 5, 9, 8, 12, 11, 4]


"""
import collections


def two_sum(nums, target):
    num_dict = {}
    for i, n in enumerate(nums):
        num_dict[n] = i

    for i, n in enumerate(nums):
        complement = target - n

        if complement in num_dict and num_dict[complement] != i:
            return [nums[i], nums[num_dict[complement]]]


def solution(coin, cards):
    def round_up(coin, cards_in_hand, cards):
        coin -= 2

        cards_in_hand.append(cards.popleft())
        cards_in_hand.append(cards.popleft())
        return coin

    cards = collections.deque(cards)

    n = len(cards)
    cards_in_hand = []
    for _ in range(int(n / 3)):
        cards_in_hand.append(cards.popleft())
    round = 0

    while len(cards) > 0 and coin > 0:
        two_card = two_sum(cards_in_hand, n + 1)
        if not two_card:
            break

        a, b = two_card
        cards_in_hand.remove(a)
        cards_in_hand.remove(b)

        coin = round_up(coin, cards_in_hand, cards)
        round += 1

    return round


coin = 4
cards = [3, 6, 7, 2, 1, 10, 5, 9, 8, 12, 11, 4]
print(solution(coin, cards))

import math


def get_gcd(array):
    gcd = array[0]
    for e in array:
        gcd = math.gcd(gcd, e)

    return gcd


def can_divide(array, n):
    for e in array:
        if e % n == 0:
            return True

    return False


def solution(arrayA, arrayB):
    gcd_a = get_gcd(arrayA)
    gcd_b = get_gcd(arrayB)

    answer = 0
    if not can_divide(arrayA, gcd_b):
        answer = max(answer, gcd_b)
    if not can_divide(arrayB, gcd_a):
        answer = max(answer, gcd_a)

    return answer

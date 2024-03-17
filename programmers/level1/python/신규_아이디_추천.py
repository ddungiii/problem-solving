import re


def filter(id):
    whitelist = ["-", "_", "."]
    new_id = ""

    for c in id:
        if c.isalpha() or c.isdigit() or c in whitelist:
            new_id += c

    return new_id


def merge_dot(id):
    while ".." in id:
        id = id.replace("..", ".")

    return id


def trim_dot(id):
    if len(id) == 0:
        return id

    if id[0] == ".":
        id = id[1:]

    if len(id) > 0 and id[-1] == ".":
        id = id[:-1]

    return id


def solution(new_id):
    # 1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
    new_id = new_id.lower()
    # 2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
    new_id = filter(new_id)
    # 3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
    new_id = merge_dot(new_id)
    # 4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
    new_id = trim_dot(new_id)
    # 5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
    if len(new_id) == 0:
        new_id = "a"
    # 6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
    #      만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
    while len(new_id) >= 16:
        new_id = new_id[:-1]
        new_id = trim_dot(new_id)
    # 7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.
    while len(new_id) < 3:
        new_id += new_id[-1]

    return new_id

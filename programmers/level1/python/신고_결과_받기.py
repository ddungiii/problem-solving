import collections


def solution(id_list, report, k):
    # 1-1. Create report count map
    # 1-2. Create mail map
    count_map = collections.defaultdict(int)
    mail_map = collections.defaultdict(list)
    for report_message in report:
        f, to = report_message.split(" ")
        if not f in mail_map[to]:
            count_map[to] += 1
            mail_map[to].append(f)

    # 2. Select count > 2 users
    ban_users = [key for key in count_map.keys() if count_map[key] >= k]

    # 3. mail it by mail map
    mail_count = [0] * len(id_list)
    for ban_user in ban_users:
        fr_users = mail_map[ban_user]
        for fr_user in fr_users:
            mail_count[id_list.index(fr_user)] += 1

    return mail_count


print(
    solution(
        ["con", "ryan"],
        ["ryan con", "ryan con", "ryan con", "ryan con"],
        3,
    )
)

print(
    solution(
        ["muzi", "frodo", "apeach", "neo"],
        ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"],
        2,
    )
)

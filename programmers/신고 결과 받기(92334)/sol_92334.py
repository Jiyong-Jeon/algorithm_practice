def solution(id_list, report, k):
    info_dict = {}
    stop_user = set()
    for id in id_list:
        info_dict[id] = [set(), 0]
    for r in report:
        user, r_user = r.split(" ")
        if not r_user in info_dict[user][0]:
            info_dict[user][0].add(r_user)
            info_dict[r_user][1] += 1
            if not r_user in stop_user and info_dict[r_user][1] >= k:
                stop_user.add(r_user)
    answer = []
    for id in id_list:
        answer.append(len(info_dict[id][0] & stop_user))

    return answer
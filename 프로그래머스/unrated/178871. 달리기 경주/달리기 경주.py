def solution(players, callings):
    # setting
    pr_dict=dict()
    rp_dict=dict()
    for i, player in enumerate(players):
        pr_dict[player] = i+1
        rp_dict[i+1] = player
    # calling
    for call in callings:
        rank = pr_dict[call]
        upper_p = rp_dict[rank-1]
        pr_dict[call] -= 1
        pr_dict[upper_p] += 1
        rp_dict[rank] = upper_p
        rp_dict[rank-1] = call
    answer = [rp_dict[i] for i in range(1, len(players)+1)]
    return answer
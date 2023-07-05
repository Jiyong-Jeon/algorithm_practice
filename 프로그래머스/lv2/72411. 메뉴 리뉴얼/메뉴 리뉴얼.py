from itertools import combinations
def solution(orders, course):
    answer = []
    orders = [''.join(sorted(list(order))) for order in orders]
    menu = sorted(list(set(''.join(orders))))
    set_orders = [set(order) for order in orders]
    for c_num in course:
        best_order_num = 0
        candidate_menu = []
        combo_list = set()
        for order in orders:
            combo_list = combo_list | set(combinations(order, c_num))
        for combo in combo_list:    
            temp = 0
            set_combo = set(combo)
            for set_order in set_orders:
                if len(set_combo & set_order) == c_num:
                    temp += 1
            if temp > best_order_num and temp > 1:
                best_order_num = temp
                candidate_menu = [''.join(combo)]
            elif temp == best_order_num and temp > 1:
                candidate_menu.append(''.join(combo))
        answer += candidate_menu
    return sorted(answer)
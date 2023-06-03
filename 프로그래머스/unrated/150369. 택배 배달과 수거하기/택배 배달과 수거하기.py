def solution(cap, n, deliveries, pickups):
    answer = 0
    while deliveries != [] or pickups != []:
        d_cap = cap
        p_cap = cap
        while deliveries != [] and deliveries[-1] == 0:
            deliveries.pop()
        while pickups != [] and pickups[-1] == 0:
            pickups.pop()
        distance_delivery = len(deliveries)
        distance_pickups = len(pickups)
        # check deliveries
        while deliveries != []:
            if deliveries[-1] > d_cap:
                deliveries[-1] -= d_cap
                break
            else:
                d_cap -= deliveries.pop()
        
        # check pickups
        while pickups != []:
            if pickups[-1] > p_cap:
                pickups[-1] -= p_cap
                break
            else:
                p_cap -= pickups.pop()
        answer += max(distance_delivery, distance_pickups) * 2
    return answer
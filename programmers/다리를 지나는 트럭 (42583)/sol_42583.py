import numpy as np
def solution(bridge_length, weight, truck_weights):
    bridge_time = []
    moving_truck = []
    time = 0
    while True:
        time += 1
        if bridge_time:
            if bridge_length == bridge_time[0]:
                moving_truck.pop(0)
                bridge_time.pop(0)

        if not (bridge_time or truck_weights or moving_truck):
            return time

        if len(moving_truck) < bridge_length and sum(moving_truck) < weight:
            if truck_weights:
                if sum(moving_truck) + truck_weights[0] <= weight:
                    moving_truck.append(truck_weights.pop(0))
                    bridge_time.append(0)
        temp = np.array(bridge_time)
        temp = temp + 1
        bridge_time = temp.tolist()

print(solution(100, 100, [10,10,10,10,10,10,10,10,10,10]))
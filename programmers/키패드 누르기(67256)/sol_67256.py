def check_hand_right(num_pos, L_pos, R_pos, hand):
    left_d = abs(num_pos[0] - L_pos[0]) + abs(num_pos[1] - L_pos[1])
    right_d = abs(num_pos[0] - R_pos[0]) + abs(num_pos[1] - R_pos[1])
    if left_d == right_d:
        if hand == 'right':
            return True
        else:
            return False
    elif left_d < right_d:
        return False
    else:
        return True


def solution(numbers, hand):
    pads = [[3, 1], [0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]  # 0 ~ 9
    L_hand = [3, 0]
    R_hand = [3, 2]
    only_left = [1, 4, 7]
    only_right = [3, 6, 9]

    answer = []
    for num in numbers:
        if num in only_left:
            L_hand = pads[num]
            answer.append('L')
        elif num in only_right:
            R_hand = pads[num]
            answer.append('R')
        else:
            if check_hand_right(pads[num], L_hand, R_hand, hand):
                R_hand = pads[num]
                answer.append('R')
            else:
                L_hand = pads[num]
                answer.append('L')

    return ''.join(answer)
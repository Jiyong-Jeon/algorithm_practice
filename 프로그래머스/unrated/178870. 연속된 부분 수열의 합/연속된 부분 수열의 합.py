def solution(sequence, k):
    answer = [0, 1000000]
    left = 0
    check_k = sequence[0]
    right = 0
    while True:
        if check_k == k:
            if answer[1] - answer[0] > right - left:
                answer = [left, right]
            right += 1
            if right >= len(sequence):
                break
            check_k += sequence[right]
        elif check_k < k:
            right += 1
            if right >= len(sequence):
                break
            check_k += sequence[right]
        else:
            check_k -= sequence[left]
            left += 1
    return answer
def solution(s):
    num_list = list(map(int, s.split(" ")))
    return ' '.join([str(min(num_list)), str(max(num_list))])
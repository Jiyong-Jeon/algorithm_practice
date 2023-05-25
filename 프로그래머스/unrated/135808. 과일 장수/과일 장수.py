def solution(k, m, score):
    score.sort(reverse=True)
    return sum([score[i+m-1]*m for i in range(0, len(score)-m+1, m)])
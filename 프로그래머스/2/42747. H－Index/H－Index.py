def solution(citations):
    citations.sort(reverse=True)
    m = 0
    for i, c in enumerate(citations):
        m = max(m, min(i+1, c))
    return m
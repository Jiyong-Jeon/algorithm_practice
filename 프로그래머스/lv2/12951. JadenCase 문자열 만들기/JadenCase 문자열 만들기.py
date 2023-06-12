def solution(s):
    return ' '.join([''.join([alpha.lower() if i != 0 else alpha.upper() for i, alpha in enumerate(word)]) for word in s.split(" ")])
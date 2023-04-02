def solution(name, yearning, photo):
    return [sum([yearning[name.index(n)] if n in name else 0 for n in p]) for p in photo]
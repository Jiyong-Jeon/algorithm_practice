def solution(brown, yellow):
    mix = (brown - 4) // 2
    for i in range(1, mix):
        if i * (mix - i) == yellow:
            return [(mix - i)+2, i+2]
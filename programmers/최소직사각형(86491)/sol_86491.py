def solution(sizes):
    x_max = 0
    y_max = 0
    for size in sizes:
        if x_max < max(size):
            x_max = max(size)
        if y_max < min(size):
            y_max = min(size)
    return x_max * y_max
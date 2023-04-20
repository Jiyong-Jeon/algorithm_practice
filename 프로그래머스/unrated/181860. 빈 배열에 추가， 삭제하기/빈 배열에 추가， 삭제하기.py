def solution(arr, flag):
    X = []
    for i, f in enumerate(flag):
        if f:
            X += [arr[i]]*(arr[i]*2)
        else:
            X = X[:-arr[i]]
    return X
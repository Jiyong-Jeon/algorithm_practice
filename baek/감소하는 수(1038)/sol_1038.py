# 조합을 활용하여 가능한 모든 수 생성
# (계산해봤을 때 약 1000개이기 때문에 가능)

from itertools import combinations
N = int(input())
l = [str(i) for i in range(10)]
temp = []
for i in range(1, 11):
    temp += [int(''.join(list(reversed(v)))) for v in list(combinations(l, i))]

temp = sorted(temp)
if N > len(temp)-1:
    print(-1)
else:
    print(temp[N])
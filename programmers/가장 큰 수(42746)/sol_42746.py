# 첫 번째 솔루션 ( 시간초과 )
import itertools
def solution(numbers):
    num2str = [str(num) for num in numbers]
    answer_list = [int(''.join(t)) for t in itertools.permutations(num2str, len(numbers))]
    answer_list.sort(reverse=True)
    return str(answer_list[0])

print(solution([3, 3, 31, 30, 34, 5, 9]))
print("--------------------------------")
# 두 번째 솔루션 실패
# def sortalgo(n_list, first, index):
#     return_list = []
#     temp = [[] for _ in range(10)]
#     for n in n_list:
#         if len(n) <= index:
#             if first > int(n[-1]):
#                 temp[first].append(n)
#             else:
#                 temp[int(n[-1])].append(n)
#             continue
#         temp[int(n[index])].append(n)
#     for i, t in enumerate(temp):
#         if len(t) >= 2:
#             t = sortalgo(t, first, index+1)
#         return_list += t
#     return return_list
#
# def solution(numbers):
#     num2str = [str(num) for num in numbers]
#     same_list = []
#     answer_list = []
#     temp = [[] for _ in range(10)]
#     for n in num2str:
#         if n in temp[int(n[0])]:
#             same_list.append(n)
#             continue
#         temp[int(n[0])].append(n)
#     for i, t in enumerate(temp):
#         if len(t) > 1:
#             temp[i] = sortalgo(t, i, 1)
#     for te in reversed(temp):
#         for t in reversed(te):
#             while t in same_list:
#                 same_el = same_list.pop(same_list.index(t))
#                 answer_list += same_el
#             answer_list += t
#     return str(int(''.join(answer_list)))
#
# print(solution([33, 32, 322, 111, 11]))

# 구글 검색..
def solution(numbers):
    num_list = list(map(str, numbers)) # 이게 속도가 조금 더 빠름
    num_list.sort(key=lambda x: x*3, reverse=True) # 30, 32, 3를 비교할 때 303030 323232 333 으로 사전적 정렬
    answer = str(int(''.join(num_list)))
    return answer

print(solution([33, 32, 322, 111, 11]))
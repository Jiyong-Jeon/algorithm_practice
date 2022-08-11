import numpy as np
from collections import Counter, deque

def can_change(word, words, depth, queue_word, queue_depth):
    word = list(word)
    words_temp = list(map(list, words))
    i = 0
    while i < len(words_temp):
        if Counter(word == np.array(words_temp[i]))[False] == 1:
            temp = ''.join(words[i])
            words.pop(i)
            words_temp.pop(i)
            i -= 1
            if not temp in queue_word:
                queue_word.append(temp)
                queue_depth.append(depth)
        i += 1

def solution(begin, target, words):
    if not target in words:
        return 0
    queue_word = deque([begin])
    queue_depth = deque([0])
    answer = 0
    while queue_word:
        word = queue_word.popleft()
        depth = queue_depth.popleft()
        if word == target:
            answer = depth
            break
        can_change(word, words, depth+1, queue_word, queue_depth)
    return answer
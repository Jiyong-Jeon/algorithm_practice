from collections import deque
import copy
def predict(pick, mineral): 
    '''
    pick : 2=dia, 1=iron, 0=stone
    mineral : 25=dia, 5=iron, 1=stone
    피로도 식 : mineral / (5**pick)
    '''
    return sum([1 if (m/(5**pick))<1 else int(m/(5**pick)) for m in mineral])
    
# dfs setting
total = 25*50+1
def dfs(temp_total, picks, minerals):
    global total
    if sum(picks) == 0 or len(minerals) == 0: # 종료조건
        if temp_total < total:
            total = temp_total
        return
    
    if picks[0] != 0:
        temp_minerals = copy.deepcopy(minerals)
        mineral = temp_minerals.popleft()
        temp_picks = copy.deepcopy(picks)
        temp_picks[0] -= 1
        pred = predict(2, mineral)
        if temp_total + pred < total:
            dfs(temp_total + pred, temp_picks, temp_minerals)
        else:
            return
    if picks[1] != 0:
        temp_minerals = copy.deepcopy(minerals)
        mineral = temp_minerals.popleft()
        temp_picks = copy.deepcopy(picks)
        temp_picks[1] -= 1
        pred = predict(1, mineral)
        if temp_total + pred < total:
            dfs(temp_total + pred, temp_picks, temp_minerals)
        else:
            return
    if picks[2] != 0:
        temp_minerals = copy.deepcopy(minerals)
        mineral = temp_minerals.popleft()
        temp_picks = copy.deepcopy(picks)
        temp_picks[2] -= 1
        pred = predict(0, mineral)
        if temp_total + pred < total:
            dfs(temp_total + pred, temp_picks, temp_minerals)
        else:
            return
    
def solution(picks, minerals):
    # setting
    minerals = [25 if m == 'diamond' else 5 if m == 'iron' else 1 for m in minerals]
    minerals = deque([minerals[i:i+5] for i in range(0, len(minerals), 5)])
    # dfs
    dfs(0, picks, minerals)
    
    return total
def solution(participant, completion):
    participant.sort()
    completion.sort()
    while completion:
        temp = participant.pop()
        if temp != completion.pop():
            return temp
    return participant[0]
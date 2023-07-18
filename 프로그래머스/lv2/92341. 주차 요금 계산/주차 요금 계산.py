from collections import defaultdict
import math

def solution(fees, records):
    acc_record = defaultdict(int)
    in_dict = dict()
    # record 
    for record in records:
        time, number, cmd = record.split(" ")
        m, s = map(int, time.split(":"))
        t = m*60 + s
        if cmd == "IN":
            in_dict[number] = t
        else:
            temp_time = t - in_dict[number]
            del in_dict[number]
            acc_record[number] += temp_time
    
    # check in list
    out_time = 23 * 60 + 59
    for number, in_time in in_dict.items():
        acc_record[number] += out_time - in_time
    
    # cal fee
    answer = []
    for number in sorted(acc_record.keys()):
        if acc_record[number] < fees[0]:
            answer.append(fees[1])
        else:
            answer.append(fees[1] + math.ceil((acc_record[number] - fees[0]) / fees[2]) * fees[3])
    
    return answer
from itertools import permutations
def cal(target_symbol_list, number, symbol):
    for target_symbol in target_symbol_list:
        new_number = []
        new_symbol = []
        pre = False
        for i in range(len(symbol)):
            if symbol[i] == target_symbol:
                if pre:
                    new_number.append(str(eval(new_number.pop()+symbol[i]+number[i+1])))
                else:
                    new_number.append(str(eval(number[i]+symbol[i]+number[i+1])))
                pre=True
            else:
                if not pre:                
                    new_number.append(number[i])
                new_symbol.append(symbol[i])
                pre=False
        if not pre:
            new_number.append(number[-1])
        number = new_number
        symbol = new_symbol
    return abs(int(number[0]))
        
def solution(expression):
    number = []
    symbol = []
    temp = ''
    for i in range(len(expression)):
        if expression[i] in ['+', '-', '*']:
            if expression[i-1] in ['+', '-', '*']:
                temp += expression[i]
            else:
                symbol.append(expression[i])
                number.append(temp)
                temp = ''
        else:
             temp += expression[i]
    number.append(temp)
    
    answer = 0
    for s in permutations(['*', '-', '+'], 3):
        temp = cal(s, number, symbol)
        if answer < temp:
            answer = temp
    return answer
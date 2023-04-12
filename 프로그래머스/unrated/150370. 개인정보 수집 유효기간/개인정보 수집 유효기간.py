def check(priv_day, today, term):
    '''
    input
    - priv_day : [year, month, day]
    - today : [year, month, day]
    
    output
    - True or False
    '''
    checking_term = 0
    checking_term += (today[0]-priv_day[0]) * 12
    checking_term += (today[1] - priv_day[1]) if (today[1] >= priv_day[1]) else (today[1] - priv_day[1])
    checking_term -= 0 if today[2] >= priv_day[2] else 1
    return True if checking_term >= term else False

def solution(today, terms, privacies):
    # setting
    today_list = list(map(int, today.split('.')))
    terms_dict = dict()
    for term in terms:
        target, month = term.split(" ")
        terms_dict[target] = int(month)
    
    # check
    answer = []
    for i, privacy in enumerate(privacies):
        day, target = privacy.split(" ")
        priv_day_list = list(map(int, day.split(".")))
        if check(priv_day_list, today_list, terms_dict[target]):
            answer.append(i+1)
    return answer
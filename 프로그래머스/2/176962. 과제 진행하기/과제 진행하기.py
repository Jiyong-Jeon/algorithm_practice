def solution(plans):
    answer = []
    # make new_plans
    new_plans = []
    for plan in plans:
        h, m = map(int, plan[1].split(":"))
        new_plans.append([plan[0], h*60+m, int(plan[2])])
    new_plans.sort(key = lambda x : x[1])
    stack_plan = [new_plans[0]]
    
    # check
    for plan in new_plans[1:]:
        diff_time = plan[1] - stack_plan[-1][1]
        while stack_plan and diff_time >= stack_plan[-1][2]:
            pre_plan = stack_plan.pop()
            diff_time -= pre_plan[2]
            answer.append(pre_plan[0])
        if stack_plan:
            stack_plan[-1][1] += diff_time
            stack_plan[-1][2] -= diff_time
        stack_plan.append(plan)
    while stack_plan != []:
        answer.append(stack_plan.pop()[0])   
    return answer
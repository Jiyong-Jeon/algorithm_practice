answer = [] 
def can_move_tickets(city, visited, tickets):
    c_m = []
    for i, ticket in enumerate(tickets):
        if i in visited:
            continue
        if ticket[0] == city:
            c_m.append((i, ticket))
    return c_m

def search(route, visited, tickets):
    global answer
    if len(visited) == len(tickets):
        if answer == []:
            answer = route
        else:
            answer = min(answer, route)
    c_m = can_move_tickets(route[-1], visited, tickets)
    if c_m == []:
        return
    for m in c_m:
        search(route+[m[1][1]], visited+[m[0]], tickets)
        
def solution(tickets):
    first_m = can_move_tickets("ICN", [], tickets)
    for i, first_ticket in first_m:
        search(first_ticket, [i], tickets)
    return answer
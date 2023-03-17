from itertools import combinations

# setting
n = int(input())
sy = [] # team synergy
for _ in range(n):
    sy.append(list(map(int, input().split(" "))))

# available team list
player = [i+1 for i in range(n)]
start_teams = []
link_teams = []
for start in combinations(player, n//2):
    link_teams.append(list(set(player) - set(start)))
    start_teams.append(list(start))

# check team diff point
def diff_point(start_team, link_team):
    start = 0
    link = 0
    for s in combinations(start_team, 2):
        start += sy[s[0]-1][s[1]-1] + sy[s[1]-1][s[0]-1]
    for l in combinations(link_team, 2):
        link += sy[l[0]-1][l[1]-1] + sy[l[1]-1][l[0]-1]

    return abs(start - link)

# search
min_point = 99999999
for i in range(len(start_teams)):
    point = diff_point(start_teams[i], link_teams[i])
    if point == 0:
        min_point = 0
        break
    elif point < min_point:
        min_point = point
print(min_point)
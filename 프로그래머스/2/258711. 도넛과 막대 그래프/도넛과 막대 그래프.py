from collections import defaultdict
def solution(edges):
    edge_in = defaultdict(int)
    edge_out = defaultdict(int)
    for edge in edges:
        edge_out[edge[0]] += 1 
        edge_in[edge[1]] += 1
    keys = max(max(edge_in.keys()), max(edge_out.keys()))

    answer = [0] * 4 # create, doughnut, 8, stick
    for key in range(1, keys+1):
        # check create node
        if edge_in[key] == 0 and edge_out[key] >= 2:
            answer[0] = key
        # check 8
        if edge_in[key] >= 2 and edge_out[key] == 2:
            answer[3] += 1
        # check stick
        if edge_in[key] >= 1 and edge_out[key] == 0:
            answer[2] += 1
    answer[1] = edge_out[answer[0]] - answer[2] - answer[3]

    return answer
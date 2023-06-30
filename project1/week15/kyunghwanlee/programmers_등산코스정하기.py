n = 6
paths = [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]]
gates = [1, 3]
summits = [5]

from collections import deque
def solution(n, paths, gates, summits):
    G = dict()
    for s, e, w in paths:
        if not G.get(s):
            G[s] =[]

        if not G.get(e):
            G[e] =[]
        G[s].append([e, w])
        G[e].append([s, w])

    mini = 10000001
    ans_s = 0
    
    dis = [mini for _ in range(n+1)]
    
    for gate in gates:
        dis[gate] = 0

    check = {}
    for s in summits:
        check[s] =0
        
    q = deque(gates)
    while q:
        cur = q.popleft()
        if check.get(cur) == 0: 
            continue

        for next, w in G[cur]:
            if dis[next] > max(dis[cur], w):
                q.append(next)
                dis[next] = max(dis[cur], w)
        
    
    for s in sorted(summits):
        if mini > dis[s]:
            mini = dis[s]
            ans_s = s

    return [ans_s, mini]




print(solution(n, paths, gates, summits))
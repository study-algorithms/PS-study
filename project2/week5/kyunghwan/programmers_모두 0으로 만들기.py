from collections import defaultdict, deque

def solution(a, edges):
    answer = 0
    if sum(a) != 0:
        return -1
    
    G = defaultdict(list)
    for s, e in edges:
        G[s].append(e)
        G[e].append(s)

    visited = [0] * len(a)
    answer =0
    queue = deque([edges[0][0]]) 
    cal = []
    while queue:
        curr = queue.popleft()
        visited[curr] = 1
        for next_node in G[curr]:
            if not visited[next_node]:
                queue.append(next_node)
                cal.append([curr, next_node])


    for parent, child in cal[::-1]:
        a[parent] += a[child]
        answer += abs(a[child])
        a[child] = 0
    return answer

a = solution([-5,0,2,1,2], [[0,1],[3,4],[2,3],[0,3]])
print(a)
# 9 

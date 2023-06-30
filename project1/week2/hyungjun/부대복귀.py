import heapq as hq

def solution(n, roads, sources, destination):
    graph = dict()
    for u,v in roads:
        if u not in graph:
            graph[u] = [v]
        else:
            graph[u].append(v)
        if v not in graph:
            graph[v] = [u]
        else:
            graph[v].append(u)
    
    dist = [10**5+1] * (n+1)
    prev = [0] * (n+1)
    dist[destination] = 0
    q = []
    hq.heappush(q, (dist[destination], destination))
    
    while q:
        d, u = hq.heappop(q)
        for linked_v in graph[u]:
            tmp = dist[u]+1
            if tmp < dist[linked_v]:
                dist[linked_v] = tmp
                prev[linked_v] = u
                hq.heappush(q, (dist[linked_v], linked_v))
    
    return [dist[d] if dist[d] != 10**5+1 else -1 for d in sources]

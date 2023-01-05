def solution(n, roads, sources, destination):
    answer = []
    
    G = [[] for _ in range(n+1)]

    for road in roads:
       G[road[0]].append(road[1])
       G[road[1]].append(road[0])

    queue = [destination]
    distance = [-1] * (n + 1)
    distance[0] = 0
    distance[destination] = 0
    
    
    while queue:
        target = queue.pop(0)
        
        for i in G[target]:
            if distance[i] == -1:
                distance[i] = distance[target] + 1
                queue.append(i)
            
            
    for source in sources:    
        answer.append(distance[source])
    return answer


solution(5, [[1, 2], [1, 4], [2, 4], [2, 5], [4, 5]], [1, 3, 5], 5)
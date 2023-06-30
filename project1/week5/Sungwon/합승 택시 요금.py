import heapq

INF = int(1e9)

def solution(n, s, a, b, fares):
    
    def dijkstra(start):
        distance = [INF] * (n+1)
        q = []
        heapq.heappush(q, (0, start))
        distance[start] = 0

        while q:
            dist, now = heapq.heappop(q)

            if distance[now] < dist:
                continue

            for i in graph[now]:
                if dist + i[1] < distance[i[0]]:
                    distance[i[0]] =  dist + i[1]
                    heapq.heappush(q, (dist+i[1], i[0]))
        return distance
    
    answer = INF
    graph = [[] for _ in range(n+1)]
    for fare in fares:
        graph[fare[0]].append((fare[1], fare[2]))
        graph[fare[1]].append((fare[0], fare[2]))
    distance = [[]]
    
    for i in range(1, n+1):
        distance.append(dijkstra(i))
    for i in range(1, n+1):
        answer = min(answer, distance[s][i] + distance[i][a] + distance[i][b])
    return answer
    

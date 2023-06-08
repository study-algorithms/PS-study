from collections import defaultdict
import heapq

def solution(n, paths, gates, summits):
    # prerequisites
    gates, summits = set(gates), set(summits) # set필요
    graph = defaultdict(list)
    for i, j, w in paths:
        graph[i].append((j, w))
        graph[j].append((i, w))
        
    def dijkstra(graph):
        hq = []
        visited = [10000001] * (n+1)
        
        for gate in gates:
            heapq.heappush(hq, (0,gate))
            visited[gate] = 0

        while hq:
            # 탐색할 거리, 노드 가져오기
            intensity, node = heapq.heappop(hq)
            # 기존 instensity보다 길면 볼 필요 없음 + node가 봉우리면 제낌
            if node in summits or intensity > visited[node]:
                continue

            # 다음 노드 추가
            for next_node, next_w in graph[node]:
                # 거리 metric = intensity
                new_intenstiy = max(intensity, next_w)
                # 지금보다 적으면 갱신
                if new_intenstiy < visited[next_node] and next_node not in gates:
                    visited[next_node] = new_intenstiy
                    heapq.heappush(hq, (new_intenstiy, next_node))
        
        return visited
    
    # get intensities
    intensities = dijkstra(graph)
    
    # get shortest intensity per summits
    answer = [0,10000001]
    for summit in sorted(summits): ## sort필요
        if intensities[summit] < answer[1]:
            answer = [summit, intensities[summit]]
    
    return answer

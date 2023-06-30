import heapq as hq

def solution(routes):
    answer = 0
    routes = [[route[1], route[0]] for route in routes]
    hq.heapify(routes)
    while routes:
        ext, _ = hq.heappop(routes)
        while routes and routes[0][1] <= ext:
            hq.heappop(routes)
        answer += 1
    return answer

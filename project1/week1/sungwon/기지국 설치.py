import math

def solution(n, stations, w):
    answer = 0
    
    now = 1
    for i in stations:
        distance = i - now - w
        if distance > 0 :
            answer += math.ceil(distance / (2 * w + 1))
        now = i + w + 1
        
    if now <= n:
        answer += math.ceil((n - now + 1)/(2 * w + 1))
        
    return answer

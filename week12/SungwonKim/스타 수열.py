from collections import Counter

def solution(a):
    answer = 0
    
    maxCnt = 0
    counter = Counter(a)
    for key, value in counter.items():
        if value <= maxCnt:
            continue
        cnt = 0
        for i in range(0, len(a)-1, 2):
            if a[i] == a[i+1]:
                continue
            if key != a[i] and key != a[i+1]:
                continue
            cnt += 1
        maxCnt = max(maxCnt, cnt)
    
    if maxCnt > 0:
        answer = maxCnt*2
    
    return answer

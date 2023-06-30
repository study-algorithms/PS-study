from collections import deque

def solution(begin, target, words):
    queue = deque([(begin, 0)])
    visited = dict()
    for word in words:
        visited[word] = False
    
    while queue:
        val = queue.popleft()
        now = val[0]
        cnt = val[1]
        visited[now] = True
        
        if now == target:
            return cnt
        
        for word in words:
            if not visited[word] and checkDiff(now, word) == 1:
                queue.append((word, cnt+1))
    
    return 0

def checkDiff(str1, str2):
    cnt = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            cnt += 1
    return cnt

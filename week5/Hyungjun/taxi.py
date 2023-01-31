def solution(n, s, a, b, fares):
    
    minFares = [[10**9]*(n+1) for _ in range(n+1)]
    for i in range(1, n+1):
        minFares[i][i]=0
    for i in range(len(fares)):
        u,v,f=fares[i]
        minFares[u][v]=f
        minFares[v][u]=f
    for mid in range(1,n+1):
        for start in range(1, n+1):
            for end in range(1,n+1):
                minFares[start][end] = min(minFares[start][end], minFares[start][mid]+minFares[mid][end])
    answer = minFares[s][a]+minFares[s][b]
    for i in range(1, n+1):
        answer = min(answer, minFares[s][i]+minFares[i][a]+minFares[i][b])
    return answer

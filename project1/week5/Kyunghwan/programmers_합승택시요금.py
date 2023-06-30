n, s, a, b = 6, 4, 5, 6
fares = [[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]]



def solution(n, s, a, b, fares):
    maxi = 200 * 100000
    
    dis = [[0 if i==j else maxi for i in range(n)] for j in range(n)]

    s, a, b = s-1, a-1, b-1

    for start, end, f in fares:
        dis[start-1][end-1] = f
        dis[end-1][start-1] = f

    
    for lov in range(n):
        for sta in range(n):
            for des in range(n):
                if dis[sta][lov] + dis[lov][des] < dis[sta][des]:
                    dis[sta][des] = dis[sta][lov] + dis[lov][des]
    
    for i in range(n):
        maxi = min(maxi, dis[s][i] + dis[i][a]+dis[i][b])


    return maxi

print(solution(n, s, a, b, fares))
def solution(n, results):
    G = [[0]*(n+1) for _ in range(n+1)]
    G_rev = [[0]*(n+1) for _ in range(n+1)]

    for result in results:
        G[result[0]][result[1]] = 1
        G_rev[result[1]][result[0]] = 1

    answer = 0
    for i in range(1, n+1):
        visited = [0] * (n+1)
        visited[i] = 1
        stack = [i]
        stack_rev = [i]

        while stack:
            for idx, val in enumerate(G[stack[-1]]):
                if val and not visited[idx]:
                    visited[idx] = 1
                    stack.append(idx)
                    break
            else:
                stack.pop()

        while stack_rev:
            for idx, val in enumerate(G_rev[stack_rev[-1]]):
                if val and not visited[idx]:
                    visited[idx] = 1
                    stack_rev.append(idx)
                    break
            else:
                stack_rev.pop()

        if sum(visited) == n:
            answer+=1
    
    
    return answer
print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))

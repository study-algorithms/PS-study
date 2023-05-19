begin = 'hit'
target = 'cog'
words = ["hot", "dot", "dog", "lot", "log"]

def isimilar(x, y):
    count = 0
    for k in range(len(x)):
        if x[k] != y[k]:
            count+=1
    return count

def solution(begin, target, words):
    words.insert(0, begin)
    G = [[0] * len(words) for _ in range(len(words))]
    for i in range(0, len(words)-1):
        for j in range(i+1, len(words)):
            if isimilar(words[i], words[j]) == 1:
                G[i][j], G[j][i] = 1, 1

    submit = 0
    answer = set()
    if target in words:
        last = words.index(target)
        stack = [last]
        visited = [0] * len(words)
        visited[last] = 1
        while stack:
            if 0 in stack:
                answer.add(len(stack) - 1)
                break
            for idx, val in enumerate(G[stack[-1]]):
                if val and not visited[idx]:
                    stack.append(idx)
                    visited[idx] = 1
                    break
            else:
                stack.pop()
                
        submit = min(answer)
    return submit

print(solution(begin, target, words))
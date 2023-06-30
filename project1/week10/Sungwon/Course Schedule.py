from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        visited = [False] * numCourses
        courses = [[] for _ in range(numCourses)]
        
        for i in prerequisites:
            courses[i[0]].append(i[1])
            indegree[i[1]] += 1

        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
    
        while q:
            now = q.popleft()
            visited[now] = True
            for i in courses[now]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    q.append(i)
        
        for i in range(numCourses):
            if visited[i] == False:
                return False
        return True

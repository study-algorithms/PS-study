# 문제 잘못 골랐습니다.. 너무 어렵습니다..
def solution(n, cores):
    if n - len(cores) <= 0 :
        return n + 1
    
    remain = [0 for _ in cores]
    while n :
        for i in range(len(cores)):
            if remain[i] == 0:
                n-=1
                if n == 0: 
                    return i+1
                remain[i] += cores[i]
        remain = list(map(lambda x: x-1, remain))
    

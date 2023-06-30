## FAIL
def solution(n, cores):
    core_status = {i : 0 for i in range(len(cores))}
    
    while n:
        for core in core_status:
            if not core_status[core]:
                core_status[core] = cores[core]
                n -= 1
            else:
                core_status[core] -= 1
                if not core_status[core]:
                    core_status[core] = cores[core]
                    n -= 1
    ret, val = 0,0
    for core in core_status:
        if core_status[core]>val:
            ret, val = core+1, core_status[core]
    return ret
## -------  
## FAIL 2
import heapq as hq

def solution(n, cores):
    core_status = []
    for i in range(1, len(cores)+1):
        hq.heappush(core_status, (0,i))
    
    t = 0
    while n:
        end_time, num = hq.heappop(core_status)
        if end_time > t:
            t = end_time
            n -= 1
        elif end_time == t:
            n -= 1   
        if n:
            hq.heappush(core_status, (t+cores[num-1], num))
        else:
            return num

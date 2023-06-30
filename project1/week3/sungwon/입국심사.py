def solution(n, times):
    times.sort()
    
    low = min(times)
    high = max(times) * n
    
    while low <= high:
        mid = (low + high) // 2
        checked = 0
        for time in times:
            checked += mid // time
        
        if checked < n:
            low = mid+1
        else:
            high = mid-1
    answer = low
    return answer

def binary_search(times, n, start, end):
    answer = 0 
    while start <= end:
        possible = 0
        mid = (start+end)//2
        possible = sum([mid//t for t in times])
        # if possible == n:
        #     return mid
        # elif possible > n:
        #     end = mid - 1
        # else:
        #     start = mid + 1
        if possible >= n:
            answer = mid
            end = mid - 1
        else:
            start = mid + 1
    return answer    
    
def solution(n, times):
    times.sort()
    lo, hi = 0, max(times)*n
    answer = binary_search(times, n, lo, hi)
    return answer

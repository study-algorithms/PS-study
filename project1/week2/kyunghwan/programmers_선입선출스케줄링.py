
def solution(n, cores):
    answer = -1
    if n < len(cores):
        return n

    
    c_sort = sorted(cores)
    n = n - len(cores)
    maxtime = c_sort[-1]*n #최악의 경우
    low, high = 1, maxtime
    
    while low < high:
        mid = (low+high) // 2
        work_done = 0
    
        for i in range(len(c_sort)):
            work_done += mid // c_sort[i]

        if work_done < n:
            low = mid+1
        
        else:
            high = mid


    temp_work_done =n

    for i in range(len(cores)):
        temp_work_done -= (high-1) // cores[i]

    
    for i in range(len(cores)):
        d, r = divmod(high, cores[i])
        if r == 0:
            temp_work_done -= 1
            if temp_work_done == 0:
                answer = i+1
                return answer




print(solution(6, [1, 2, 3]))




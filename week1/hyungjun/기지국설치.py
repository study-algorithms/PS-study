def solution(n, stations, w):
    answer = 0
    answer += get_minimum_number(stations[0]-w-1, w)
    answer += get_minimum_number(n-(stations[len(stations)-1]+w), w)
    for i in range(len(stations)-1):
        answer += get_minimum_number((stations[i+1]-stations[i]-1)-(2*w),w)
    return answer

def get_minimum_number(l, w):
    if l <= 0:
        return 0
    if 2*w+1 >= l:
        return 1
    else:
        return l//(2*w+1)+1 if l%(2*w+1) else l//(2*w+1)

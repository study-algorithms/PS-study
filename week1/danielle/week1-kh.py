def windows(l:list, n)->list:
    res = []
    for i,v in enumerate(l):
        if i == 0 :
            res.append(v[0]-1)
            new_start = v[1]+1
            if len(l)==1:
                res.append(n+1-new_start)
        else:
            temp = v[0] - new_start
            new_start = v[1]+1
            res.append(temp)

        if v[1]>n:
            break
    return res

def required(inp,range) -> int:
    if inp%range==0:
        return inp//range
    else:
        return (inp//range)+1

def solution(n, stations, w):
    cover_range = 2*w + 1
    covered = [(i-w,i+w) for i in stations]
    uncovered = windows(covered,n)
    required_station = [required(i,cover_range) for i in uncovered]
    return sum(required_station)

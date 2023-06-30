from collections import Counter

a= [0,3,3,0,7,2,0,2,2,0]
def solution(a):
    max_len = -1
    for k, v in Counter(a).most_common():
        if max_len > v * 2:
            continue

        idx, cnt = 0, 0

        while idx < len(a)-1:
            if (a[idx] != a[idx+1]) and k in [a[idx], a[idx+1]]:
                cnt+=2
                idx+=2
            else:
                idx+=1

        if cnt > max_len:
            max_len = cnt

    return max_len



# 하나 빼고 다됨
# def solution(a):
#     common = Counter(a).most_common(1)[0][0]
    
#     idx, cnt = 0, 0

#     while idx < len(a)-1:
#         if (a[idx] != a[idx+1]) and common in [a[idx], a[idx+1]]:
#             cnt+=2
#             idx+=2
#         else:
#             idx+=1

    
#     return cnt

print(solution(a))
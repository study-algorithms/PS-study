import math

# 처음 시도, log(on^2)인 구간이 있어서 실패한듯

def solution(n, stations, w):
    answer = 0

    for i in range(len(stations)-1):
        not_affected = (stations[i+1]-w-1) - (stations[i]+w+1) +1
        if not_affected > 0:
            answer+= math.ceil(not_affected/(2*w+1))
    fron_stat =  stations[0] -w -1 
    back_stat =  n - (stations[-1]+w+1)+1

    if fron_stat > 0:
        answer+= math.ceil(fron_stat/(2*w+1))

    if back_stat >0:
        answer+= math.ceil(back_stat/(2*w+1))

    print(answer)
    return answer 


# def solution(n, stations, w):
#     check = [0] * n
#     answer = 0
#     for st in stations:
#         if st - w < 0:
#             check[0:st+w-1] = [1] * (st+w)
        
#         elif st+w > n-1:
#             check[st-1:n] = [1] * (n-st)
        
#         else:
#             check[st-w-1: st+w-1] = [1] * (2*w+1)
        
#     print(check)


#     start=0
#     while (start <= len(check)-1):
#         if not check[start]:
#             length = 0
#             for i in range(start, len(check)):
#                 if i == len(check)-1:
#                     answer+= math.ceil(length/(2*w+1))
#                     print(answer)
#                     return answer
                    
#                 if check[i]:
#                     start= i
#                     answer+= math.ceil(length/(2*w+1))
#                     break
#                 length+=1
#         else:
#             start+=1

#     return answer


solution(11, [4, 11], 1)
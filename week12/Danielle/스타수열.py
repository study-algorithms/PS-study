from collections import Counter
def solution(a):
    cnts = Counter(a)
    answer = -1
    for k in cnts.keys():
        if cnts[k] <= answer:
            continue
        # star 수열 찾기
        idx = 0
        temp_answer = 0
        
        while idx < len(a) - 1:
            if (a[idx] != k and a[idx+1] != k) or (a[idx] == a[idx+1]):
                idx += 1
                continue
            temp_answer += 1
            idx += 2
        answer = temp_answer
    
    return max(0, answer*2)

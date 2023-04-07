def solution(scores):
    wanho = scores[0]
    wanho_sum = sum(scores[0])
    scores = sorted(scores, key = lambda x: (-x[0], x[1]))
    thresh = answer = 0
    
    for score in scores:
        if wanho[0] < score[0] and wanho[1] < score[1]:
            return -1
        if thresh <= score[1]:
            thresh = score[1]
            if sum(score) > wanho_sum:
                answer +=1
    return answer + 1

scores = [[2,2],[1,4],[3,2],[3,2],[2,1]]

def solution(scores):
    answer = 1
    wan, wan_score = scores[0], sum(scores[0]) 
    scores = sorted(scores, key=lambda x:(-x[0], x[1]))
    before_partner_point = 0
    for score in scores:
        # 완호 인센 x
        if wan[0] < score[0] and wan[1] < score[1]:
            return -1

        # 다른애들 인센 x
        if score[1] < before_partner_point:
            continue
    
        if wan_score < sum(score) :
            answer+=1
        before_partner_point = score[1]

    return answer

print(solution(scores))
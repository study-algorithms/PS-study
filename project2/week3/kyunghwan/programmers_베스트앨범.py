def solution(genres, plays):
    answer = []
    compare = []
    info = dict()
    for i in range(len(genres)):
        compare.append([genres[i], plays[i], i])
        if genres[i] not in info.keys():
            info[genres[i]] = plays[i]
        else:
            info[genres[i]] += plays[i]
    info = sorted(info.items(), key=lambda x: -x[1])
    compare = sorted(compare, key=lambda x: (-x[1], x[2]))
    answer = []
    for j in info:
        count = 0
        for k in compare:
            if count >= 2:
                break
            if k[0] == j[0]:
                answer.append(k[2])
                count +=1
        
    return answer


a = solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500])
print(a)
#[4, 1, 3, 0]

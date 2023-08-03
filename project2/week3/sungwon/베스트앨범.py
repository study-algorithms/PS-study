def solution(genres, plays):
    def sumItem(item):
        total = 0
        for val in item[1]:
            total += val[1]
        return total
    
    answer = []
    dic = dict()
    for i in range(len(genres)):
        if dic.get(genres[i]) != None:
            dic[genres[i]].append((i, plays[i]))
        else:
            dic[genres[i]] = [(i, plays[i])]
    
    sorted_dict = sorted(dic.items(), key = sumItem, reverse=True)
    for key, value in sorted_dict:
        sorted_value = sorted(value, key = lambda value: value[1], reverse=True)
        answer.append(sorted_value[0][0])
        if len(value) >= 2:
            answer.append(sorted_value[1][0])
            
    return answer

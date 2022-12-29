def solution(user_id, banned_id):
    answer = 1
    
    group = [[] for _ in range(len(banned_id))]
    
    for bidx in range(len(banned_id)):
        for uidx in range(len(user_id)):
            if len(banned_id[bidx]) == len(user_id[uidx]):
                matched = True
                for i in range(len(banned_id[bidx])):
                    if banned_id[bidx][i] != user_id[uidx][i] and banned_id[bidx][i] != '*':
                        matched = False
                        break
                if matched == True:
                    group[bidx].append(user_id[uidx])

    for i in range(len(group)):
        answer *= len(group[i])

    print(answer)
    for i in range(len(group)):
        for j in range(i+1, len(group)):
            for k in range(len(group[i])):
                for l in range(len(group[j])):
                    print(group[i][k])
                    print(group[j][l])
                    print('\n')
                if group[i][k] == group[j][l]:
                    answer -= 1
            
    return answer

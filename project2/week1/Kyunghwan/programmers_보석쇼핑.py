gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]

def solution(gems):
    start, end = 0, 0
    possi = [0, 0]
    mini = 9999999999
    cnt = len(set(gems))
    temp = dict()
    while end < len(gems):
        if gems[end] not in temp:
            temp[gems[end]] =1
        else:
            temp[gems[end]]+=1

        end +=1

        if len(temp) == cnt:
            while start < end:
                if temp[gems[start]] != 1:
                    temp[gems[start]] -=1
                    start +=1

                else:
                    if end - start < mini:
                        mini = end-start
                        possi[0], possi[1] = start+1, end
                    break

    return possi

print(solution(gems))

sticker = [14, 6, 5, 11, 3, 9, 2, 10]


def solution(sticker):
    if len(sticker) <= 3:
        return max(sticker)


    sums_first = [0] * len(sticker)
    sums_second = [0] * len(sticker)

    # open first sticker
    sums_first[0] = sticker[0]
    sums_first[1] = sticker[0]
    sums_first[-1] = sticker[0]
    for i in range(2, len(sticker)-1):
        sums_first[i] = max(sticker[i] + sums_first[i-2], sums_first[i-1])

    # open second sticker
    sums_second[1] = sticker[1] 
    for i in range(2, len(sticker)):
        sums_second[i] = max(sticker[i] + sums_second[i-2], sums_second[i-1])
    
    

    answer = max(max(sums_first), max(sums_second))
    return answer


print(solution(sticker))
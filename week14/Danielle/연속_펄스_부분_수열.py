def solution(sequence):
    
    def purse(seq, num):
        res = []
        for i in seq:
            res.append(i*num)
            num *= -1
        return res
    
    def dynamic_programming(arr):
        cache = [None] * len(arr)
        cache[0] = arr[0]
        for i in range(1, len(arr)):
            cache[i] = max(0, cache[i-1]) + arr[i]
        return max(cache)
    
    # two cases
    temp1 = purse(sequence,1)
    temp2 = purse(sequence,-1)
    # answer
    answer = 0
    answer = max(answer, dynamic_programming(temp1))
    answer = max(answer, dynamic_programming(temp2))
    return answer

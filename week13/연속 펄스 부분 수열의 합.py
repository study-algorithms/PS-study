def solution(sequence):
    maxSum1, maxSum2 = [0] * (len(sequence)+1), [0] * (len(sequence)+1)
    turn = 1
    for i, v in enumerate(sequence):
        maxSum1[i+1] = max(maxSum1[i] + v*turn, v*turn)
        maxSum2[i+1] = max(maxSum2[i] - v*turn, -1*v*turn)
        turn = -1 * turn
    answer = max(max(maxSum1), max(maxSum2))
    return answer

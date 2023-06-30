# import numpy as np

# def solution(sequence):
#     pul = np.array([sequence[i] if i%2==0 else -sequence[i] for i in range(len(sequence))])
#     cum = pul.cumsum()
    
#     answer = max(abs(max(cum)), abs(min(cum)), max(cum) - min(cum))

#     return answer


def solution(sequence):
    pul = [sequence[i] if i%2==0 else -sequence[i] for i in range(len(sequence))]
    cum = []
    for p in pul:
        if not len(cum):
            cum.append(p)
        else:
            cum.append(cum[-1] + p)
        
    
    answer = max(abs(max(cum)), abs(min(cum)), max(cum) - min(cum))

    return answer
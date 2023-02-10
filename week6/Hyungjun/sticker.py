def solution(sticker):
    l=len(sticker)
    d, d2=[s for s in sticker], [s for s in sticker]
    if l == 1:
        return sticker[0]
    d[1] = d[0]
    d2[0] = 0
    for i in range(2, l):
        if i < l-1:
            d[i], d2[i] = max(d[i-1], d[i-2] + sticker[i]), max(d2[i-1], d2[i-2]+sticker[i])
        else:
            d2[i] = max(d2[i-1], d2[i-2]+sticker[i])
            d[i] = max(d[i-1], d[i-2])
        
    return max(d[l-1],d2[l-1])

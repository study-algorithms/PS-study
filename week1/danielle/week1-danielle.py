import itertools

def match(ref, inp)->bool:
    if len(ref) != len(inp):
        return False
    for i in range(len(ref)):
        if ref[i] == '*':
            continue
        if ref[i] != inp[i]:
            return False
    return True

def solution(user_id, banned_id)->int:
    answer = []
    match_dict = {}
    res = []
    
    # getting nCr
    for ban in list(set(banned_id)):
        match_dict[ban] = [u for u in user_id if match(ban, u)]
        nCr_temp = list(itertools.combinations(match_dict[ban], banned_id.count(ban)))
        res.append(nCr_temp)
    
    # filtering
    for r in list(itertools.product(*res)):
        if len(set(r))==len(set(banned_id)):
            answer.append(r)
            
    return len(answer)

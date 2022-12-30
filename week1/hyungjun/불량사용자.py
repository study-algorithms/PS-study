# DFS
def solution(user_id, banned_id):
    answer = 0
    list_set = set()
    answer += dfs(0, user_id, banned_id, list_set)
    return answer

def check(user_id, banned_id):
    if len(user_id) != len(banned_id):
        return False
    for s1, s2 in zip(user_id, banned_id):
        if s2 == '*':
            continue
        if s1 != s2:
            return False
    return True

visit_set = set()

def dfs(banned_id_idx, user_id, banned_id, list_set):
    ret = 0
    if banned_id_idx == len(banned_id):
        if hash(tuple(sorted(list_set))) not in visit_set:
            visit_set.add(hash(tuple(sorted(list_set))))
            return 1
        else:
            return ret
    # find next possible id list from user_id
    for id in user_id:
        if id not in list_set:
            if check(id, banned_id[banned_id_idx]):
                list_set.add(id)
                ret += dfs(banned_id_idx+1, user_id, banned_id, list_set)
                list_set.remove(id)
    return ret
                
        

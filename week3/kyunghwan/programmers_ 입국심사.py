def immigrate(low, high, req_members, gates):
    global mini
    runningtime = (low+high) // 2
    people = 0   #게이트 통과한 사람
    for i in range(len(gates)):
        people += runningtime // gates[i]
    if people >= req_members:
        people_previous = 0
        for i in range(len(gates)):
            people_previous += (runningtime-1) // gates[i]
        if people_previous < req_members:
            mini = runningtime
            return

        immigrate(low, runningtime, req_members, gates)
    else:
        immigrate(runningtime, high, req_members, gates)

mini = 9999
def solution(n, times):
    gates = times
    maxtime = max(gates) * n
    immigrate(0, maxtime, n, gates)
    return mini
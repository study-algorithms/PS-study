# n, t, m, timetable = 2, 10, 2, ["09:10", "09:09", "08:00"]
# n, t, m, timetable = 10, 60, 45, ["23:59","23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"]
# n, t, m, timetable = 1, 1, 1, ["23:59"]
# n, t, m, timetable = 1, 1, 5, ["00:01", "00:01", "00:01", "00:01", "00:01"]
n, t, m, timetable =2, 1, 2, ["09:00", "09:00", "09:00", "09:00"]



from datetime import timedelta
import datetime

def solution(n, t, m, timetable):
    buses = [datetime.datetime(2000,1,1,9)]

    for i in range(n-1):
        now = buses[-1] + datetime.timedelta(minutes=(t))
        buses.append(now)


    timetable = sorted(timetable)


    for i in range(n):
        cur = buses[i]
        cnt = 0

        while timetable and datetime.datetime(2000,1,1,int(timetable[0].split(':')[0]), int(timetable[0].split(':')[1]))<= cur and cnt<m:
            tar = timetable.pop(0)
            cnt+=1

    if cnt == m:
        answer = datetime.datetime(2000,1,1,int(tar.split(':')[0]), int(tar.split(':')[1])) - datetime.timedelta(minutes=1)


    else:
        answer = cur


    final = ''
    if len(str(answer.hour)) < 2:
        final= final+ '0'+ str(answer.hour) + ':'
    else:
        final= final+ str(answer.hour) + ':'


    if len(str(answer.minute)) < 2:
        final= final+ '0'+ str(answer.minute)
    else:
        final= final+ str(answer.minute)

    return final


a = solution(n, t, m, timetable)
print(a)
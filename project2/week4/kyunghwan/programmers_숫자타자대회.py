loc = {
    '1':[0, 0], '2':[0, 1], '3': [0, 2],
    '4': [1, 0], '5':[1, 1], '6': [1, 2],
    '7':[2, 0], '8':[2, 1], '9': [2, 2],
    '*': [3, 0], '0':[3, 1], '#': [3, 2]
}

G = []
for i in range(12):
    temp = []
    if i == 10:
        cur_num = '*'
        
    elif i == 11:
        cur_num = '#'

    else:
        cur_num = str(i)

    for j in range(12):
        if j == 10:
            nex_num = '*'
        
        elif j == 11:
            nex_num = '#'
        
        else:
            nex_num = str(j)

        cur_pos, nex_pos = loc[cur_num], loc[nex_num]

        dis = [abs(nex_pos[0] - cur_pos[0]), abs(nex_pos[1] - cur_pos[1])]

        if dis[0] == 0 and dis[1] == 0:
            l_eft = 1
        elif dis[0] ==0 or dis[1] == 0:
            l_eft = dis[0]*2 + dis[1]*2
            
        elif dis[0] == 1 and dis[1]== 1:
            l_eft = 3
            
        elif (dis[0] ==1 or dis[1] ==1) and (dis[0]>1 or dis[1] >1):
            l_eft = min(dis[0], dis[1]) * 3 + (max(dis[0], dis[1])-1) * 2
            
        elif dis[0] == 2 and dis[1] == 2:
            l_eft = 3 * 2
        else:
            l_eft = min(dis[0], dis[1]) * 3 + (max(dis[0], dis[1])-2) *2
        
        temp.append(l_eft)
    G.append(temp)


def num_conv(value):
    if value == '*' or value == 10:
        value = 10
    elif value == '#'or value == 11:
        value = 11
    else:
        value = int(value)
    return value


def solution(numbers):
    record = {('4','6') : 0}

    for n in numbers:
        n_record = {}
        for cur, cnt in record.items():
            left, right = cur
            if left == n:
                if (n, right) not in n_record or n_record[(n, right)] > G[num_conv(left)][num_conv(int(n))] + cnt:
                    n_record[(n, right)] = cnt + G[num_conv(left)][num_conv(n)]
            elif right == n:
                if (left, n) not in n_record or n_record[(left, n)] > G[num_conv(right)][num_conv(int(n))] + cnt:
                    n_record[(left, n)] = cnt + G[num_conv(n)][num_conv(right)]
            else: 
                if (n, right) not in n_record or n_record[(n, right)] > G[num_conv(left)][num_conv(int(n))] + cnt:
                    n_record[(n, right)] = cnt + G[num_conv(left)][num_conv(n)]

                if (left, n) not in n_record or n_record[(left, n)] > G[num_conv(right)][num_conv(int(n))] + cnt:
                    n_record[(left, n)] = cnt + G[num_conv(n)][num_conv(right)]
        
        record = n_record
       
    return min(record.values())

numbers = "1756"
print(solution(numbers))
# 10

numbers = "5123"
print(solution(numbers))
# 8

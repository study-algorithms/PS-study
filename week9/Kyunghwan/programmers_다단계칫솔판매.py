enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
referral = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
seller = ["young", "john", "tod", "emily", "mary"]
amount = [12, 4, 2, 5, 10]


from collections import defaultdict
def solution(enroll, referral, seller, amount):
    connect = defaultdict()
    money = defaultdict()
    answer = []

    for i in range(len(enroll)):
        connect[enroll[i]] = referral[i]
        money[enroll[i]] = 0

    for i in range(len(seller)):
        target = seller[i]
        tar_mon = amount[i] * 100
        
        while True:
            if int(0.1 * tar_mon) > 0:
                money[target] += int(tar_mon - int(0.1 * tar_mon))
            else:
                money[target] += tar_mon
                break


            if connect[target] !='-':
                target = connect[target]
            else:
                break

            tar_mon = int(0.1 * tar_mon)

    for k, v in money.items():
        answer.append(v)
        
    return answer




print(solution(enroll, referral, seller, amount))
         
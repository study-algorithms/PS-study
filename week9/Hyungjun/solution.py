import math

def solution(enroll, referral, seller, amount):
    answer = [0 for _ in range(len(enroll))]
    id = {name: i for i, name in enumerate(enroll)}
    for i in range(len(seller)):
        income = amount[i] * 100
        fee = math.floor(income * 0.1)
        answer[id[seller[i]]] += (income - fee)
        ref = referral[id[seller[i]]]
        income = fee
        while ref != "-" and income > 0:
            _i = id[ref]
            fee = math.floor(income * 0.1)
            answer[id[ref]] += (income - fee)
            ref = referral[id[ref]]
            income = fee
    return answer
  
  # https://school.programmers.co.kr/learn/courses/30/lessons/77486

a= [-16,27,65,-2,58,-92,-71,-68,-61,-33]

def solution(a):
    check = [0] * len(a)

    left, right = 1000000001, 1000000001

    for i in range(len(a)):
        if a[i] < left:
            left = a[i]
            check[i] = 1

        if a[-1-i] < right:
            right = a[-1-i]
            check[-1-i] = 1

    print(check)
    return check.count(1)


print(solution(a))
numpad = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [-1, 0, -1]]

def solution(numbers):
    def findNum(num):
        for i in range(4):
            for j in range(3):
                if numpad[i][j] == num:
                    return i,j
    
    def getCost(x1, y1, x2, y2):
        diffX, diffY = abs(x1-x2), abs(y1-y2)
        cost = 0
        if diffX == 0 and diffY == 0:
            cost += 1
        else:
            if diffX > 0 and diffY > 0:
                temp = min(diffX, diffY)
                cost += temp * 3
                diffX -= temp
                diffY -= temp
            cost += diffX * 2 + diffY * 2
        return cost
    
    totalCost = 0
    leftCurrX, leftCurrY, rightCurrX, rightCurrY  = 1, 0, 1, 2
    numList = list(map(int, str(numbers)))
    
    for num in numList:
        x, y = findNum(num)
        leftCost = getCost(leftCurrX, leftCurrY, x, y)
        rightCost = getCost(rightCurrX, rightCurrY, x, y)
        if leftCost <= rightCost:
            print("left, cost: %d" %leftCost)
            totalCost += leftCost
            leftCurrX = x
            leftCurrY = y
        else:
            print("right, cost: %d" %rightCost)
            totalCost += rightCost
            rightCurrX = x
            rightCurrY = y

    return totalCost

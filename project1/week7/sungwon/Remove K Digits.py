class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        strNum = str(num)
        if len(strNum) == k:
            return "0"
        checkPoint = 0
        for i in range(k):
            for j in range(checkPoint, len(strNum)-1):
                if int(strNum[j]) > int(strNum[j+1]):
                    strNum = strNum[:j] + strNum[j+1:]
                    if j > 0:
                        checkPoint = j-1
                    break
                if j == len(strNum)-2:
                    strNum = strNum[:j+1] + strNum[j+2:]
                    checkPoint = j-1
        return str(int(strNum))

# time limit
class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        def ismonotone(num):
            digits = [n for n in str(num)]
            for i in range(len(digits)-1):
                if digits[i] > digits[i+1]:
                    return False
            return True
        def way2monotone(num):
            digits = [n for n in str(num)]
            for i in range(len(digits)-1):
                if digits[i] > digits[i+1]:
                    #######
                    return False
            return num
        while True:
            if ismonotone(n):
                return n
            else:
                n -= 1

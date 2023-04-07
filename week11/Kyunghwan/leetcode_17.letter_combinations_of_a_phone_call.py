digits = "23"
class Solution:
    def letterCombinations(self, digits):
        letters = dict()
        num = 97
        for i in range(2, 10):
            if i in [7, 9]:
                letters[i] = [chr(num), chr(num+1), chr(num+2), chr(num+3)]
                num+=4

            else:
                letters[i] = [chr(num), chr(num+1), chr(num+2)]
                num+=3


        answer = []
        for digit in digits:
            if not answer:
                answer = letters[int(digit)]
            else:
                temp = []
                for a in answer:
                    for l in letters[int(digit)]:
                        temp.append(a+l)
                answer = temp
        return answer
    
a = Solution()
print(a.letterCombinations(digits))


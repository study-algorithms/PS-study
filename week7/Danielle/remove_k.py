# wrong
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        # you just cant swap their place
        #''.join(sorted(num)[:-k])

        def without(lst, idx):
            return ''.join([x for i, x in enumerate(lst) if i != idx])

        def onestep(number):
            temp = sys.maxsize
            for i in range(len(number)):
                temp = min(int(without(number,i)), temp)
            return str(temp)

        for i in range(k):
            if k >= len(num):
                return "0"
            else:
                res = onestep(num)
                num = res
        
        return res

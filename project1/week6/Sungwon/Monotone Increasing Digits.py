class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        str_n = str(n)
        list_n = list(str_n)
        for i in range(len(list_n)-1, 0, -1):
            if int(list_n[i]) < int(list_n[i-1]):
                if i == 1 and list_n[i-1] == '1':
                    list_n.pop(0)
                    i -= 1
                else:
                    list_n[i-1] = str(int(list_n[i-1])-1)
                for j in range(i, len(list_n)):
                    list_n[j] = '9'
        return int(''.join(list_n))

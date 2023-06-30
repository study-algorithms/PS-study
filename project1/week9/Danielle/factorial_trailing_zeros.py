class Solution:
    def trailingZeroes(self, n: int) -> int:
        # how many 5 in this number?
        answer = 0
        bar = 1
        while n > bar:
            bar *= 5
            answer += n//bar
        return answer

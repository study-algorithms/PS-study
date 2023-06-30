from collections import Counter

s = "bbcaac"
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counter = Counter(s)
        checked = [0] * 26
        stack = [s[0]]
        counter[s[0]] -= 1
        checked[ord(s[0])-97]=1
        for i in range(1, len(s)):
            letter = s[i]
            counter[letter] -= 1
            if checked[ord(letter)-97]:
                continue

            while stack and letter < stack[-1] and (counter[stack[-1]] > 0):
                trash = stack.pop()
                checked[ord(trash)-97]= 0
            
            stack.append(letter)
            checked[ord(letter)-97]=1
           
 
        return ''.join(stack)


a=Solution()
print(a.removeDuplicateLetters(s))

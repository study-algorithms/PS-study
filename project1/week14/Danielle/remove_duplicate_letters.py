class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # return ''.join(sorted(set(s)))
        counter = collections.Counter(s)
        seen = set()
        stack = []

        for char in s:
            counter[char] -= 1
            if char in seen:
                continue            
            
            while stack and char < stack[-1] and counter[stack[-1]] > 0 :
                seen.remove(stack.pop())
            stack.append(char)
            seen.add(char)

            
        return ''.join(stack)

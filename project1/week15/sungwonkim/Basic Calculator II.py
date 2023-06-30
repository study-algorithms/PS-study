class Solution:
    def calculate(self, s: str) -> int:
        num, op, stack = 0, '+', []

        for i, v in enumerate(s):
            if v.isdigit():
                num = num*10 + int(v)
            
            if v in '+-*/' or i == len(s)-1:
                if op == '+':
                    stack.append(num)
                elif op == '-':
                    stack.append(-num)
                elif op == '*':
                    stack.append(stack.pop() * num)
                elif op == '/':
                    stack.append(stack.pop() // num)
                op = v
                num = 0
        
        return sum(stack)

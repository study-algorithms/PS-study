class Solution:
    def calculate(self, s: str) -> int:
        st = []
        s=s.replace(" ", "")
        num = 0
        oper = ''

        def execute(st, oper, num):
            if oper == '':
                st.append(num)
            elif oper == '+':
                st.append(num)
            elif oper == '-':
                st.append(-num)
            elif oper == '*':
                st.append(st.pop()*num)
            elif oper == '/':
                st.append(
                    int(st.pop()/num)
                )

        for c in s:
            if c.isdigit():
                num = num*10+int(c)
            else:
                execute(st, oper, num)
                num=0
                oper=c
        execute(st, oper, num)
        return sum(st)
                

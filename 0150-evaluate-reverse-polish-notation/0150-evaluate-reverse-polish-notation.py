class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk=[]
        for val in tokens:
            if val=='-':
                fv=int(stk.pop())
                sv=int(stk.pop())
                stk.append(sv-fv)
            elif val=='*':
                fv=int(stk.pop())
                sv=int(stk.pop())
                stk.append(sv*fv)
            elif val=='+':
                fv=int(stk.pop())
                sv=int(stk.pop())
                stk.append(sv+fv)
            elif val=='/':
                fv=int(stk.pop())
                sv=int(stk.pop())
                stk.append(int(sv/fv))
            else:
                stk.append(val)
        return int(stk[0])
            
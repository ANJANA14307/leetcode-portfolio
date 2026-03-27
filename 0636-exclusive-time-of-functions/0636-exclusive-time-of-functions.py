class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        stk=[]
        res=[0]*n
        prev_time=0
        for log in logs:
            parts=log.split(':')
            lid=int(parts[0])
            state=parts[1]
            ts=int(parts[2])
            if state=='start':
                if stk:
                    res[stk[-1]]+=ts-prev_time
                stk.append(lid)
                prev_time=ts
            else:
                res[stk[-1]]+=ts-prev_time+1
                stk.pop()
                prev_time=ts+1
        return res
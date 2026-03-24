class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        nl=[]
        idx=0
        for i in range(1,n+1):
            if idx==len(target):
                break
            if target[idx]==i:
                nl.append("Push")
                idx+=1
            else:
                nl.extend(["Push","Pop"])
        return nl
    


        
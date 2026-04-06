class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n=len(prices)
        lst=list(prices)
        for i in range(n):
            for j in range(i+1,n):
                if prices[j]<prices[i] or prices[j]==prices[i]:
                    lst[i]=prices[i]-prices[j]
                    break
        return lst
        
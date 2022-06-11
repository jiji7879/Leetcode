class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mi = 10001
        result = 0
        for i in prices:
            if i < mi:
                mi = i
                ma = 0
            elif i > ma:
                ma = i
                if ma-mi > result:
                    result = ma-mi
        return result

"""version 2
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxcur = 0
        maxsofar = 0
        i = 1
        while i < len(prices):
            maxcur = max(0, maxcur + prices[i]-prices[i-1])
            maxsofar = max(maxcur, maxsofar)
            i+=1
        return maxsofar
"""

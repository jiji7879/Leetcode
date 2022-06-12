#dynamic programming
class Solution:
    def __init__(self):
        self.min = inf
    def coinChange(self, coins: List[int], amount: int) -> int:
        partialsol = [inf for i in range(amount+1)]
        partialsol[0] = 0
        i=1
        while i <= amount:
            mini = inf
            for j in coins:
                if i-j >=0 and partialsol[i-j] != -1:
                    mini = min(mini, partialsol[i-j]+1)
            if mini == inf:
                partialsol[i] = -1
            else:
                partialsol[i] = mini
            i+=1
        return partialsol[amount]

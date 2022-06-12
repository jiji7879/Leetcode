class Solution:
    def climbStairs(self, n: int) -> int:
        partialsol = [1, 1]
        i=2
        while i <= n:
            partialsol.append(partialsol[0]+partialsol[1])
            del partialsol[0]
            i+=1
        return partialsol[1]

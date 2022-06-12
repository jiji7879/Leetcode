class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        firstprod = [1]
        for i in nums:
            firstprod.append(firstprod[-1]*i)
        lastprod = [1]
        nums.reverse()
        for i in nums:
            lastprod.append(lastprod[-1]*i)
        nums.reverse()
        solution = []
        j = 0
        while j < len(nums):
            solution.append(firstprod[j]*lastprod[-j-2])
            j+=1
        return solution

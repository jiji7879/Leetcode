"""version1
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
"""
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        firstprod = [1]
        for i in nums:
            firstprod.append(firstprod[-1]*i)
        firstprod.pop()
        print(firstprod)
        lastprod = 1
        j=1
        while j < len(nums):
            print(firstprod[-j])
            print("next")
            firstprod[-j] *= lastprod
            print(firstprod[-j])
            lastprod *= nums[-j]
            print(lastprod)
            j+=1
        firstprod[0] *= lastprod
        return firstprod

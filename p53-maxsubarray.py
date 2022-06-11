class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currentsum = nums[0]
        currentmax = nums[0]
        i=1
        while i < len(nums):
            if currentsum > 0:
                currentsum += nums[i]
            else:
                currentsum = nums[i]
            currentmax = max(currentmax, currentsum)
            i+=1
        return currentmax

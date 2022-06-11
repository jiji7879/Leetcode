class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = []
        i=0
        while i < len(nums):
            if target - nums[i] not in seen:
                seen.append(nums[i])
            else:
                return [seen.index(target - nums[i]), i]
            i+=1
        

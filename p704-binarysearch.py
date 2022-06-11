class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums)==0:
            return -1
        return self.shelper(nums, target, 0, len(nums)-1)
    def shelper(self, nums: List[int], target: int, start: int, end: int):
        if end-start == 0 or end-start == 1:
            if nums[start] == target:
                return start
            elif nums[end] == target:
                return end
            return -1
        half = (start + end) // 2
        if nums[half] == target:
            return half
        elif nums[half] < target:
            return self.shelper(nums, target, half+1, end)
        else:
            return self.shelper(nums, target, start, half-1)

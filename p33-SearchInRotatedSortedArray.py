class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.searchhelper(nums, target, 0, len(nums)-1)
    def searchhelper(self, nums: List[int], target: int, start: int, stop: int) -> int:
        print(nums[start:stop+1])
        if start==stop:
            if nums[start]==target:
                return start
            return -1
        elif start == stop-1:
            if nums[start]==target:
                return start
            elif nums[stop]==target:
                return stop
            return -1
        mid = (start+stop)//2
        if nums[mid] == target:
            return mid
        #we're in the weird case. [4,5,1,2,3]
        elif nums[mid] < nums[start]:
            if target == nums[start]:
                return start
            #if bigger than start or less then mid
            elif target > nums[start] or target < nums[mid]:
                return self.searchhelper(nums, target, start, mid-1)
            else:
                return self.searchhelper(nums, target, mid+1, stop)
        #target = 1,7, nums=[6,7,8,1,2]
        elif nums[mid] > target:
            if nums[start] > target:
                return self.searchhelper(nums, target, mid+1, stop)
            return self.searchhelper(nums, target, start, mid-1)
        elif nums[mid] < target:
            if nums[start] < target:
                return self.searchhelper(nums, target, mid+1, stop)
            return self.searchhelper(nums, target, start, mid-1)
        else:
            print("C")
            return 0
    

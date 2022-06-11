# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        return self.BadHelper(1, n)
    def BadHelper(self, start: int, end: int):
        if start==end:
            return start
        elif start == end-1:
            if isBadVersion(start):
                return start
            else:
                return end
        half = (start+end)//2
        if isBadVersion(half):
            return self.BadHelper(start, half)
        return self.BadHelper(half+1, end)
        

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cursub = []
        sol = 0
        i=0
        while i < len(s):
            cursub.append(s[i])
            if cursub.index(s[i])!=len(cursub)-1:
                cursub = cursub[cursub.index(s[i])+1:]
            else:
                if len(cursub) > sol:
                    sol = len(cursub)
            i+=1
        return sol

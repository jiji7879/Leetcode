"""version 1
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        slist = []
        tlist = []
        for char in s:
            slist.append(char)
        for char in t:
            tlist.append(char)
        slist.sort()
        tlist.sort()
        if slist == tlist:
            return True
        return False
"""
#version 2
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        slist = [0 for i in range(26)]
        tlist = [0 for i in range(26)]
        for char in s:
            slist[ord(char) - ord('a')] += 1
        for char in t:
            tlist[ord(char) - ord('a')] += 1
        if slist == tlist:
            return True
        return False

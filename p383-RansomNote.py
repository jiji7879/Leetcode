class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        lichar = [0 for i in range(26)]
        for char in magazine:
            lichar[ord(char)-ord('a')] += 1
        for char in ransomNote:
            lichar[ord(char)-ord('a')] -= 1
            if lichar[ord(char)-ord('a')] == -1:
                return False
        return True

        

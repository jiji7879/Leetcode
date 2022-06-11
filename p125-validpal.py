class Solution:
    def isPalindrome(self, s: str) -> bool:
        condensed = ""
        for char in s:
            if char.isalnum():
                condensed += char.lower()
        if condensed == "":
            return True
        i=0
        while i < len(condensed) // 2:
            if condensed[i] != condensed[-i-1]:
                return False
            i+=1
        return True

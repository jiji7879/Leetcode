class Solution:
    def longestPalindrome(self, s: str) -> int:
        answer=0
        oddswitch=0
        i=0
        while i < 26:
            b=s.count(chr(65+i))
            answer += b // 2
            if oddswitch==0 and b % 2 == 1:
                oddswitch=1
            i+=1
        j=0
        while j < 26:
            b=s.count(chr(97+j))
            answer += b // 2
            if oddswitch==0 and b % 2 == 1:
                oddswitch=1
            j+=1
        return answer*2+oddswitch

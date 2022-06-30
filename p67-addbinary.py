class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if a=="0" and b=="0":
            return "0"
        alpha = max(len(a), len(b))
        binarray = ["0" for i in range(alpha+1)]
        i=0
        while i < alpha:
            onecount = 0
            if i < len(a) and a[-i-1]=="1":
                onecount += 1
            if i < len(b) and b[-i-1]=="1":
                onecount += 1
            if binarray[-i-1] == "1":
                onecount += 1
            if onecount // 2 == 1:
                binarray[-i-2] = "1"
            if onecount % 2 == 1:
                binarray[-i-1] = "1"
            else:
                binarray[-i-1] = "0"
            i+=1
        j=0
        while binarray[j] == "0":
            j+=1
        string = ""
        for k in range(j, len(binarray)):
            string += binarray[k]
        return string
        

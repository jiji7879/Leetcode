class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        numlist = []
        for item in tokens:
            if item == "+":
                second = numlist.pop()
                first = numlist.pop()
                numlist.append(first+second)
            elif item == "-":
                second = numlist.pop()
                first = numlist.pop()
                numlist.append(first-second)
            elif item == "*":
                second = numlist.pop()
                first = numlist.pop()
                numlist.append(first*second)
            elif item == "/":
                second = numlist.pop()
                first = numlist.pop()
                div = first//second
                if div < 0 and div != first/second:
                    numlist.append(div + 1)
                else:
                    numlist.append(div)

            else:
                numlist.append(int(item))
        return numlist[0]

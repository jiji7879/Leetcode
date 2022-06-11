class Solution:
    def isValid(self, s: str) -> bool:
        needed = [0]
        for char in s:
            if char == '(':
                needed.append(')')
            elif char == '{':
                needed.append('}')
            elif char == '[':
                needed.append(']')
            elif char != needed.pop():
                return False
        return (needed == [0])

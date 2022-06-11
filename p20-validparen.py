"""version 1
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
"""
"""version 2
class Solution:
    def isValid(self, s: str) -> bool:
        needed = []
        for char in s:
            if char == '(':
                needed.append(')')
            elif char == '{':
                needed.append('}')
            elif char == '[':
                needed.append(']')
            elif len(needed) == 0 or char != needed.pop():
                return False
        return (needed == [])
"""
#version 3 with dict
class Solution:
    def isValid(self, s: str) -> bool:
        d = {'(':')', '{':'}', '[':']'}
        needed = []
        for char in s:
            if char in d:
                needed.append(char)
            elif len(needed) == 0 or d[needed.pop()] != char:
                return False
        return (needed == [])

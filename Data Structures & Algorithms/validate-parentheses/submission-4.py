class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for char in s:
            if char == '{' or char == '(' or char == '[':
                stack.append(char)
            else:
                if not stack:
                    return False
                close = stack.pop()
                if ((close == '{' and char == '}') or 
                (close == '[' and char == ']')  or 
                (close == '(' and char == ')')):
                    continue
                else:
                    stack.append(char)
        if stack:
            return False
        else:
            return True
        
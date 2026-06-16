class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {")" : "(", "}" : "{", "]" : "["}

        if len(s) < 2:
            return False

        for i in range(len(s)):
            if s[i] not in closeToOpen:
                stack.append(s[i])
            else:
                if len(stack) == 0:
                    return False
                openBracket = stack.pop()
                if closeToOpen[s[i]] != openBracket:
                    return False
        
        if len(stack) != 0:
            return False
        else:
            return True
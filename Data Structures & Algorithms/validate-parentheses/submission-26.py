class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openToClose = {"(": ")", "{": "}", "[": "]"}
        for i in range(len(s)):
            if s[i] in openToClose.keys():
                stack.append(s[i])
            else:
                try:
                    openBracket = stack.pop()
                except:
                    return False
                if openToClose[openBracket] != s[i]:
                    return False
                    
        if len(stack) != 0:
            return False
        else:
            return True
        
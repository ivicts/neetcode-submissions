class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ''

        for i in range(len(s)):
            if s[i].isalnum():
                newStr += s[i].lower()
        
        for i in range(len(newStr)//2):
            if newStr[i] != newStr[len(newStr)-i-1]:
                return False

        return True
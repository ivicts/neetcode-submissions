class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s = ''.join(c.lower() for c in s if c.isalnum())
        j = len(s) - 1
        print(s)
        for i in range(len(s)//2):
            if s[i] != s[j]:
                return False
            j-= 1 
        return True 
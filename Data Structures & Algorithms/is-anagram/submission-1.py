class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter = {}
        for c in s:
            if c not in counter:
                counter[c] = 1
            else:
                counter[c] = counter[c] + 1

        for c in t:
            if c not in counter:
                return False
            else:
                counter[c] = counter[c] - 1
            
        for key, value in counter.items():
            if value > 0:
                return False

        return True
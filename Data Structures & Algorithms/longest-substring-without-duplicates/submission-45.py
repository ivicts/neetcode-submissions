class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        longest = 0
        substr_len = 0

        if len(s) == 0:
            return 0

        substr = {}

        for r in range(len(s)):
            if s[r] not in substr:
                substr[s[r]] = r
                substr_len += 1
            else:
                old_l = l
                new_l = substr[s[r]] + 1
                if new_l > old_l:
                    l = new_l
                substr_len += -(l - old_l) + 1
                substr[s[r]] = r
            #print(l, r, s[l:r + 1], substr_len, len(s[l:r + 1]), substr)
            longest = max(longest, substr_len)

        return longest

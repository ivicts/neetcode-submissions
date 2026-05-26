class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        # r = 1
        longest = 1
        substr_len = 1

        if len(s) == 0:
            return 0

        substr = {}
        substr[s[0]] = 0

        for r in range(1, len(s)):
            if s[r] not in substr:
                substr[s[r]] = r
                substr_len += 1
            else:
                old_l = l
                new_l = substr[s[r]] + 1
                if new_l > old_l:
                    l = new_l
                substr_len += -(l - old_l) + 1
                # if substr_len < 1:
                #     substr_len = 1
                substr[s[r]] = r
            #print(l, r, s[l:r + 1], substr_len, len(s[l:r + 1]), substr)
            longest = max(longest, substr_len)

        return longest

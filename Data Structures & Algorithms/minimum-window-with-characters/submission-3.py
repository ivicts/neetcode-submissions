class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        res = math.inf
        resstring = ""
        t_freq = {}

        for i in range(len(t)):
            t_freq[t[i]] = t_freq.get(t[i], 0) + 1

        print(t_freq)
        #print("A")
        
        while (l < len(s)):
            t_freq_copy = t_freq.copy()
            # if l < 3:
            #     print(l)
            if s[l] in t_freq_copy:
                #pass
                t_freq_copy[s[l]] = t_freq_copy[s[l]] - 1

                if t_freq_copy[s[l]] == 0:
                    t_freq_copy.pop(s[l], None)
                    if len(t_freq_copy) == 0:
                        if 1 < res:
                            res = 1
                            resstring = s[l : l + 1]

                for r in range(l + 1, len(s)):
                    print(l, r)
                    if s[r] in t_freq_copy:
                        t_freq_copy[s[r]] = t_freq_copy[s[r]] - 1
                        print(t_freq_copy)
                        if t_freq_copy[s[r]] == 0:
                            t_freq_copy.pop(s[r], None)
                            print(t_freq_copy)
                            if len(t_freq_copy) == 0:
                                if (r - l + 1) < res:
                                    res = r - l + 1
                                    resstring = s[l : r + 1]
                
            
            l += 1

        return resstring
class Solution:
    def minWindow(self, s: str, t: str) -> str:
       
        if t == "":
            return ""

        res = [-1, -1]
        resLen = float("infinity")
        
        countT = {}
        window = {}

        for i in range(len(t)):
            countT[t[i]] = countT.get(t[i], 0) + 1

        have, need = 0, len(countT)
        l = 0
        for r in range(len(s)):
            c = s[r]

            if c in countT:
                window[c] = window.get(c, 0) + 1

                if countT[c] == window[c]:
                    have += 1


            while (have == need):
                #print(l, r)
                if (r - l + 1) < resLen:
                    res = [l, r + 1]
                    resLen = r - l + 1
                    #print(res, resLen)
                
                if s[l] in countT:
                    window[s[l]] -= 1

                    if window[s[l]] < countT[s[l]]:
                        have -= 1
                l+= 1


        if resLen != float("infinity"):
            return s[res[0]: res[1]]
        else:
            return ""

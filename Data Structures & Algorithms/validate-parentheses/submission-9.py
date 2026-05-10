class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_par = ["(", "{", "["]
        close_par = [")", "}", "]"]
        par_dict = dict(zip(open_par, close_par))

        if (len(s)% 2) != 0 or s[0] not in open_par:
            return False

        for i in range(len(s)):
            print(stack)
            if s[i] in open_par:
                stack.append(par_dict[s[i]])
            else:
                try:
                    s_pop = stack.pop()
                    print(s_pop, s[i])
                    if (s_pop != s[i]):
                        return False
                except:
                    return False

        if len(stack) != 0:
            return False
        return True
class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for i in range(len(strs)):
            encoded_string += str(len(strs[i])) + "#" + strs[i]
            
        return encoded_string

    def decode(self, s: str) -> List[str]:

        l = 0
        decoded_string = []
        #print("encoded ", s)

        strlen = ""
        while (l < len(s)):
            if s[l] != "#":
                strlen += s[l]
                l+= 1
            elif s[l] == "#":
                #print("strlen", strlen)
                if strlen == 0:
                    decoded_string.append("")
                    l+= 1
                    strlen = ""
                else:
                    decoded_string.append(s[l + 1:l + 1 +  int(strlen)])
                    l += int(strlen) + 1
                    strlen = ""

        return decoded_string
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_dict = {}

        if len(s) < len(t):
            first_str = s
            second_str = t
        else:
            first_str = t
            second_str = s

        for i in range(len(first_str)):
            if first_str[i] not in count_dict:
                count_dict[first_str[i]] = 1
            else:
                count_dict[first_str[i]] += 1
        
        #print(count_dict)
        for j in range(len(second_str)):
            if second_str[j] not in count_dict:
                return False
            else:
                count_dict[second_str[j]] -= 1
                if count_dict[second_str[j]] < 0:
                    return False

        return True
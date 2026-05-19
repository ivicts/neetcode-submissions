from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counter_dict = defaultdict(list)

        for i in range(len(strs)):
            s = strs[i]
            count = [0]*26
            for j in range(len(s)):
                count[ord(s[j]) - ord("a")] += 1
            
            counter_dict[tuple(count)].append(s)

        #print(counter_dict.values())
        return list(counter_dict.values())
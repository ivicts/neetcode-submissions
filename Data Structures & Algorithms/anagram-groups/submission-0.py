from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counter_list = []
        for i in range(len(strs)):
            str_cur = strs[i]
            counter_list.append(Counter(str_cur))
            #count_dict_cur = self.counter_dict(str_cur)

        return_list = []

        skipped_i = []
        for i in range(len(counter_list)):
            if i not in skipped_i:
                return_now = []
                return_now.append(strs[i])
                j = i + 1
                while (j < len(strs)):
                    if counter_list[i] == counter_list[j]:
                        return_now.append(strs[j])
                        skipped_i.append(j)
                    j += 1
                return_list.append(return_now)
        
        return return_list

    def counter_dict(self, str_curr: str) -> Dict[str]:
        count_dict = {}
        for i in range(len(str_curr)):
            if str_curr[i] not in count_dict:
                count_dict[str_curr[i]] = 1
            else:
                count_dict[str_curr[i]] += 1

        return count_dict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter_dict = {}
        dict_final = defaultdict(list)
        max_counter = -float("inf")

        for i in range(len(nums)):
            n = nums[i]
            if n not in counter_dict:
                counter_dict[n] = 1
            else:
                counter_dict[n] += 1

        for key, val in counter_dict.items():
            if val > max_counter:
                max_counter = val
            dict_final[val].append(key)

        final_ret = []
        counter = max_counter
        while (len(final_ret) < k):
            if counter in dict_final:
                final_ret.extend(dict_final[counter])
            
            counter -= 1

        return final_ret[:k]
            

        
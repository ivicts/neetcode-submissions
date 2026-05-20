class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_dict = {}
        count_list = [[] for i in range(len(nums) + 1)]
        res = []

        for n in nums:
            count_dict[n] = 1 + count_dict.get(n, 0)

        for n, count in count_dict.items():
            count_list[count].append(n)

        for i in range(len(count_list) - 1, 0, -1):
            #print(i)
            for j in count_list[i]:
                res.append(j)

                if len(res) == k:
                    return res
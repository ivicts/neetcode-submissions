class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums) - 1

        if N == 0:
            return nums[0]
        nums_1 = nums[:-1]
        cache_1 = [-1]*N

        nums_2 = nums[1:]
        cache_2 = [-1]*N

        def dfs_1(i):
            if i >= N:
                return 0
            else:
                if cache_1[i] == -1:
                    cache_1[i] = max(nums_1[i] + dfs_1(i + 2), dfs_1(i + 1))

                return cache_1[i]
            
        def dfs_2(i):
            if i >= N:
                return 0
            else:
                if cache_2[i] == -1:
                    cache_2[i] = max(nums_2[i] + dfs_2(i + 2), dfs_2(i + 1))

                return cache_2[i]
            
        return max(dfs_1(0), dfs_2(0))
class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        cache = [-1]*N
        def dfs(i):
            if i >= N:
                return 0
            else:
                if cache[i] == -1:
                    cache[i] = max(nums[i] + dfs(i + 2), dfs(i + 1))
                return cache[i]

        return dfs(0)
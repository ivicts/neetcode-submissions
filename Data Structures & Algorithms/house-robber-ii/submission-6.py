class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums) - 1

        if N == 0:
            return nums[0]

        nums_1 = nums[:-1]
        cache_1 = [-1]*N

        nums_2 = nums[1:]
        cache_2 = [-1]*N

        def dfs(i, version):
            if i >= N:
                return 0
            else:
                if version == 1:
                    if cache_1[i] == -1:
                        cache_1[i] = max(nums_1[i] + dfs(i + 2, 1), dfs(i + 1, 1))

                    return cache_1[i]
                elif version == 2:
                    if cache_2[i] == -1:
                        cache_2[i] = max(nums_2[i] + dfs(i + 2, 2), dfs(i + 1, 2))

                    return cache_2[i]
            

            
        return max(dfs(0, 1), dfs(0, 2))
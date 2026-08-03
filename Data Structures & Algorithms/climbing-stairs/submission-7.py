class Solution:
    def climbStairs(self, n: int) -> int:
        cache = [-1]*n

        def dfs(n: int) -> int:
            if n <= 2:
                cache[n - 1] = n
            elif cache[n - 1] == -1:
                cache[n - 1] = dfs(n - 1) + dfs(n - 2)
            
            return cache[n - 1]
            
        return dfs(n)
            
class Solution:
    def climbStairs(self, n: int) -> int:
        cache = [-1]*n
        # cache[0] = 1
        # cache[1] = 2

        def dfs(n: int) -> int:
            if n == 1:
               cache[0] = 1
            elif n == 2:
                cache[1] = 2
            elif cache[n - 1] == -1:
                cache[n - 1] = dfs(n - 1) + dfs(n - 2)
            
            return cache[n - 1]
            
        return dfs(n)
            
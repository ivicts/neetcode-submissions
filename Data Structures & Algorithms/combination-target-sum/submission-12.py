class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []
        nums.sort()

        def dfs(sums, start, summation):
            nonlocal res
            if summation == target:
                res.append(sums.copy())
                return
            elif summation > target:
                return
            else:
                for i in range(start, len(nums)):
                    if summation + nums[i] > target:
                        break
                    sums.append(nums[i])
                    dfs(sums, i, summation + nums[i])
                    sums.pop()

        dfs([], 0, 0)

        return res
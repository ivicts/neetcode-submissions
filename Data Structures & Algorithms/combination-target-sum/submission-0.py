class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []

        def dfs(sums, start):
            nonlocal res
            summation = sum(sums)
            print(sums, summation, start)
            if summation == target:
                print("target ", sums)
                res.append(sums.copy())
                return
            elif summation > target:
                return
            else:
                for i in range(start, len(nums)):
                    # print(start)
                    sums.append(nums[i])
                    summation = sum(sums)
                    if summation <= target:
                        dfs(sums, i)
                    sums.pop()

        for i in range(len(nums)):
            dfs([nums[i]], i)

        return res
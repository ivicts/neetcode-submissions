class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []
        nums.sort()

        def dfs(sums, start, summation):
            nonlocal res
            #summation = sum(sums)
            #print(sums, summation, start)
            if summation == target:
                #print("target ", sums)
                res.append(sums.copy())
                return
            elif summation > target:
                return
            else:
                for i in range(start, len(nums)):

                    if summation + nums[i] > target:
                        break
                    # print(start)
                    sums.append(nums[i])
                    #summation += nums[i]
                    dfs(sums, i, summation + nums[i])
                    # else:
                    #     break
                    sums.pop()

        # for i in range(len(nums)):
        #     dfs([nums[i]], i)
        dfs([], 0, 0)

        return res
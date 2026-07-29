class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        resList = []
        #print(nums)

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i -1]:
                #print(i)
                continue
            j = i + 1
            k = len(nums) - 1
            target = -nums[i]
            while (j < k):
               
                summation = nums[j] + nums[k]
                #print(summation , target)
                #print(i, j, k)
                if (summation < target):
                    j += 1
                elif summation > target:
                    k -= 1
                elif (summation == target):
                    resList.append([nums[i], nums[j], nums[k]])
                    #print(i, j, k)
                    j += 1
                    while j < k and nums[j] == nums[j-1]:
                        j+= 1
                    #print(resList)

        return resList 
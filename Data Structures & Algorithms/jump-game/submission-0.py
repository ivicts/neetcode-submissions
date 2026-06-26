class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        goal = n - 1

        for i in range(n - 2, -1, -1):
            num = nums[i]
            #print(num)
            if i + num >= goal:
                goal = i

        if goal == 0:
            return True
        else:
            return False
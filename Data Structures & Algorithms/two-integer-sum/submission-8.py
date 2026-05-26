class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums) - 1
        nums_dict = {}
        

        for i in range(len(nums)):
            nums_dict[nums[i]] = i

        for i in range(len(nums)):
            rem = target - nums[i]
            if rem in nums_dict:
                if nums_dict[target-nums[i]] != i:
                    return [i, nums_dict[target-nums[i]]]
                
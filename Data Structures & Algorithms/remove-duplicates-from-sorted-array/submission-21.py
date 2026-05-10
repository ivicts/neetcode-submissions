class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique = sorted(set(nums))
        nums[:len(unique)] = unique
        return len(unique)
        # for i in range(len(nums)):

        #     if (nums[i] == nums[i + 1]):
        #         nums[i] = nums[i + 1]
                
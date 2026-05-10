class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count_dict = {}
        for i in range(len(nums)):
            num = nums[i]
            if num not in count_dict:
                count_dict[num] = 0
            else:
                count_dict[num] += 1
                return True

        return False
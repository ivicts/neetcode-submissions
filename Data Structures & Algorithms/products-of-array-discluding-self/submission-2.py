class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre_prod = 1
        suff_prod = 1
        res = []
        prefix = []
        suffix = []
        for i in range(len(nums)):
            pre_prod *= nums[i]
            suff_prod *= nums[len(nums) - 1 - i]
            prefix.append(pre_prod)
            suffix.append(suff_prod)

        print(prefix, suffix)
        for i in range(len(nums)):
            if i == 0:
                res.append(suffix[len(nums) - i - 2])
            elif i == (len(nums) - 1):
                res.append(prefix[i - 1])
            else:
                res.append(prefix[i - 1]*suffix[len(nums) - i - 2])

        return res
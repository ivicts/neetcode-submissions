class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        maxLength = 0

        for i in range(len(nums)):
            if nums[i] - 1 not in nums:
                # START from here
                seqLength = 1
                num = nums[i]
                while (num + 1 in nums):
                    num += 1
                    seqLength += 1
                maxLength = max(maxLength, seqLength)

        return maxLength
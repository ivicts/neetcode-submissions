class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counter = {}
        for x in nums:
            if x not in counter:
                counter[x] = 1
            else:
                return True
        return False
        
class Solution:
    def search(self, nums: List[int], target: int, offset = 0) -> int:
        lenNums = len(nums)
        midIdx = lenNums//2
        
        if lenNums == 1:
            if nums[midIdx] != target:
                return -1

        #print(offset)
        if nums[midIdx] == target:
            return midIdx + offset
        elif target < nums[midIdx]:
            return self.search(nums[:midIdx], target)
        elif target > nums[midIdx]:
            return self.search(nums[midIdx:], target, midIdx + offset)
        else:
            return -1
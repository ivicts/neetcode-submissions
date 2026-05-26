class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l = 0
        r = len(nums) - 1

        #print("S")
        while (l <= r):

            if nums[l] < nums[r]:
                r = l
                break
            elif l == r:
                break

            m = l + (r - l)//2

            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m

        #print("r ", r)
        # min index = r
        leftRes = self.binSearch(nums, target, 0, r)
        rightRes = self.binSearch(nums, target, r, len(nums) - 1)

        if leftRes != -1:
            return leftRes
        elif rightRes != -1:
            return rightRes
        else:
            return -1

    def binSearch(self, nums: List[int], target: int, l: int, r: int) -> int:

        # l = 0
        # r = len(nums) - 1

        while (l <= r):

            m = l + (r - l)//2

            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            elif nums[m] == target:
                return m

        return -1
                

            
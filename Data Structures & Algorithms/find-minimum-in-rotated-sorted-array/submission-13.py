class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        l, r = 0, len(nums) - 1
        counter = 0

        while (l <= r):
            
            m = l + ((r - l)//2)

            if nums[m-1] > nums[m]:
                #SORTED
                return nums[m]
            elif nums[l] < nums[m] and nums[m] < nums[r]:
                return nums[l]
            elif nums[r] < nums[m]:
                l = m + 1
            elif nums[m] < nums[l]:
                r = m - 1
            elif (l == m):
                return nums[l]

        
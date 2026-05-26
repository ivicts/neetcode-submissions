class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l = 0
        r = len(nums) - 1

        while (l <= r):

            m = l + ((r - l))//2
            print(l, m, r)

            if nums[m] == target:
                return m
            # elif (nums[l] < nums[r]):
            #     if nums[m] > target:
            #         r = m - 1
            #     else:
            #         l = m + 1

            #left sorted part
            elif (nums[l] <= nums[m]):
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1

            # right sorted part
            elif (nums[r] > nums[m]):
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
            else:
                return -1
            #elif nums[m] > target and nums[l] > nums[r]:

        return -1
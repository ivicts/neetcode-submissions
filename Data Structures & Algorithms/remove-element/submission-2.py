class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        counter = 0
        idx = []
        for i in range(len(nums)):
            if (nums[i] == val):
                # idx.append(i)
                pass
                #counter+= 1
            else:
                nums[counter] = nums[i]
                counter+= 1
                # if counter > 0:
                #     nums[idx[counter]] = nums[i]
                # counter+= 1
        print(nums, counter)
        return counter

        
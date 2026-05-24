class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        l = 0
        r = len(numbers) - 1

        while (l < r):
            summation = numbers[l] + numbers[r]

            if summation < target:
                l += 1
            elif summation > target:
                r -= 1
            elif target == summation:
                return [l+ 1, r + 1]
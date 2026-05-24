class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        l = 0
        r = len(heights) - 1
        maxAmount = 0

        while l < r:
            barHeights = min(heights[l], heights[r])
            amount = barHeights*(r - l)
            if amount > maxAmount:
                maxAmount = amount

            if heights[l] <= heights[r]:
                l += 1
            elif heights[r] < heights[l]:
                r -= 1

        return maxAmount

            

            
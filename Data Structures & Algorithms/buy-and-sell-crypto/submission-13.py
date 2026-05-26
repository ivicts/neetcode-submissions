class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        l = 0
        maxProfit = 0
        minPrice = prices[0]

        if len(prices) == 1:
            return 0

        for i in range(1, len(prices)):
            minPrice = min(minPrice, prices[i-1])
            maxProfit = max(maxProfit, prices[i] - minPrice)

        return maxProfit
            
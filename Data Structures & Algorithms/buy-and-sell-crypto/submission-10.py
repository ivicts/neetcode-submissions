class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        l = 0
        #r = len(prices) - 1
        maxProfit = 0

        if len(prices) == 1:
            return 0

        for s in range(1, len(prices)):
            buyPrices = min(prices[:s])
            maxProfit = max(maxProfit, prices[s] - buyPrices)
            # b = 0
            # buyPrices = prices[b]
            # while (b < s):
            #     buyPrices = min(buyPrices, prices[b]


      

        return maxProfit
            
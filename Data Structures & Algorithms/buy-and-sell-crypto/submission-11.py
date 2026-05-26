class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        l = 0
        #r = len(prices) - 1
        maxProfit = 0
        minPrice = prices[0]

        if len(prices) == 1:
            return 0

        for i in range(1, len(prices)):
            minPrice = min(minPrice, prices[i-1])
            #print(buyPrices, prices[i])
            maxProfit = max(maxProfit, prices[i] - minPrice)
            # b = 0
            # buyPrices = prices[b]
            # while (b < s):
            #     buyPrices = min(buyPrices, prices[b]


      

        return maxProfit
            
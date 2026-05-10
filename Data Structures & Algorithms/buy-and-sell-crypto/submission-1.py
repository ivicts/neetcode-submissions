class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profits = []
        for i in range(1, len(prices)):
            sell_val = prices[i]
            min_buy_val = min(prices[:i])
            max_profits.append(sell_val - min_buy_val)

        if len(max_profits) == 0:
            return 0
        max_profit = max(max_profits)
        if max_profit < 0:
            return 0
        else:
            return max_profit
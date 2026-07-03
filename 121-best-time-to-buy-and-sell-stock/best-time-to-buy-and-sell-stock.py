class Solution:
    def maxProfit(self, price: List[int]) -> int:
        buy = price[0]
        profit = 0
        for i in range(1, len(price)):
            if price[i] < buy:
                buy = price[i]
            elif price[i] - buy > profit:
                profit = price[i] - buy
        return profit
from typing import List

class Solution:
    # Time Limit Exceeded
    def maxProfit_1(self, prices: List[int]) -> int:
        profit = 0
        for i in range(0, len(prices), 1):
            for j in range(len(prices)-1, i, -1):
                #print("i:", i, "j:", j)
                #print("Profit:", profit)
                if prices[j] - prices[i] > profit:
                    profit = prices[j] - prices[i]
        
        return profit

    def maxProfit(self, prices: List[int]) -> int:
        current_min = prices[0]
        profit = 0
        for price in prices:
            if price < current_min:
                current_min = price
            elif price - current_min > profit:
                profit = price - current_min

        return profit
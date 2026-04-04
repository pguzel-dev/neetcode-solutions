# Time: O(n)
# Space: O(1)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest_buy = float('inf')
        max_profit = 0
        for price in prices:
            lowest_buy = min(price, lowest_buy)
            max_profit = max(max_profit, price - lowest_buy)
        return int(max_profit)
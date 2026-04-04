# Brute Force
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_prof = 0
        for left in range(len(prices)):
            profit = 0
            for right in range(left+1, len(prices)):
                holder = prices[right] - prices[left]
                profit = max(profit, holder)
            max_prof = max(max_prof, profit)

        return max_prof
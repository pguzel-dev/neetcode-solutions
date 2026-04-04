# Brute Force
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_prof = 0
        for left in range(len(prices)):
            for right in range(left+1, len(prices)):
                profit = prices[right] - prices[left]
                max_prof = max(max_prof, profit)
        return max_prof
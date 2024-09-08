# LeetCode - 121

# Brute Force, we can try for all buy and sell combination, Tx-> O(n*2)

# We will think about the Sell on a ith day, so to gain max profit we should know the min price day before it.
# so if we know the minimum price on every point for buy we can calculate the max profit.
# Tx-> O(n) 
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        pastMin = prices[0]
        maxProfit = 0

        for i in range(len(prices)):
            pastMin = min(pastMin,prices[i])
            maxProfit = max(maxProfit,prices[i]-pastMin)
        return maxProfit
# Container With Most Water - LeetCode 11

# In Bruteforce we can take all combinations of heights and find the max water, Tx->O(n^2) 

# we will take two pointers from left and right.
# calcualte the water in between, if left height smaller than right move left ahead, else move right
# Tx-> O(n)
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        res = 0

        while l < r:
            res = max(res, min(heights[l], heights[r]) * (r - l))
            if heights[l] < heights[r]:
                l += 1
            elif heights[r] <= heights[l]:
                r -= 1
            
        return res
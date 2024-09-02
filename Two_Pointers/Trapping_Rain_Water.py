# Trapping Rain Water - LeetCode 42

# Brute force will take O(n^2) to iterate on the every index and then find left right max for it.

# Better approach
# we will create 2 list pre and post to store left and right max of every index.
# then we will just take min(left max, right max) - height of curr index
# Tx-> O(n) , Sx-> O(n)
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l = 0
        r = len(height)-1

        # Premax
        pre = [0]*n
        for i in range(1,n):
            pre[i] = max(pre[i-1],height[i-1])
        

        # Postmax
        post = [0]*n
        for i in range(n-2,-1,-1):
            post[i] = max(post[i+1],height[i+1])

        total_water = 0
        curr_water = 0
        for i in range(n):
            curr_water = min(pre[i],post[i])-height[i]
            if curr_water > 0:
                total_water = total_water + curr_water

        return total_water
    
# Most Optimal Approach
# we will create 2 pointers, left and right
# the trick of considering only one side of boundary is for eg if leftMax < rightMax
# No need to check the rightMax for that now as we are taking the min of them anyways.
# Tx-> O(n), Sx-> O(1)
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l = 0
        r = len(height)-1

        leftMax = height[l]
        rightMax = height[r]

        total_water = 0

        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                total_water += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                total_water += rightMax - height[r]
        return total_water
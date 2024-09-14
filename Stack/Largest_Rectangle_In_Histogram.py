# Leetcode - 84

# we will create 2 list for leftsmaller and rightSmaller using stack
# Tx-> O(n), Sx->O(n)

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = []
        leftSmaller = [0]*n
        rightSmaller = [0]*n
        maxArea = float('-inf')

        for i in range(n):
            while(stack and heights[stack[-1]]>=heights[i]):
                stack.pop()
            
            if not stack:
                leftSmaller[i] = 0
            else:
                leftSmaller[i] = stack[-1] + 1
            stack.append(i)
        
        stack = []

        for i in range(n-1,-1,-1):
            while(stack and heights[stack[-1]]>=heights[i]):
                stack.pop()
            
            if not stack:
                rightSmaller[i] = n-1
            else:
                rightSmaller[i] = stack[-1] - 1
            stack.append(i)

        for i in range(n):
            maxArea = max(maxArea,(rightSmaller[i]-leftSmaller[i]+1)*heights[i])
        
        return maxArea










        
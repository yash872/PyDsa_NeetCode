# LeetCode - 239

# Tx-> O(k*(n-k))
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        left = 0
        right = k-1

        while right < len(nums):
            output.append(max(nums[left:right+1]))
            left+=1
            right+=1
        return output

# Most Optimal Approach

# Using deque() we will maintain a decresing queue and take out max from starting element of queue.
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = deque()  # index
        l = r = 0

        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            if l > q[0]:
                q.popleft()

            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1
            r += 1

        return output

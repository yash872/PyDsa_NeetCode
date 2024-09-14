# LeetCode - 704

# Basic Binary Search Alogorithm
# Tx-> O(logn)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        low = 0
        high = n-1

        while low <= high:
            mid = low + (high-low)//2
            
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                high = mid-1
            else:
                low = mid+1
        return -1
        
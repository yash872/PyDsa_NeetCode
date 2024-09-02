# Two Sum - LeetCode 1

# we can iterate nested loop nad find the combination but Tx-> O(n^2)

# create hashmp of values,index and search the diff (target-value) in it, Tx-> O(n), Sx-> O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}  # val -> index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
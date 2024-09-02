# Product of Array Excluding self - LeetCode238

# we can't use division else we can do it by total product divided by num[i]
# we can do it by cumulative product
# create cumulative product array from both side and create final product, extra Sx-> O(n+n)


# we will use output array to store prefix and postfix products to save space
# Tx-> O(n)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums))

        for i in range(1, len(nums)):
            res[i] = res[i-1] * nums[i-1]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res

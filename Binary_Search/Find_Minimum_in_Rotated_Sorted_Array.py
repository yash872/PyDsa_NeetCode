# To find the minimum number in rotated array
# first we will find the mid, if mid num >= the extreme left num
# it means the mid is part of the left sorted array and for themin num we have to look at right


class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = float('inf')
        l, r = 0, len(nums)-1

        while l <= r:
            if nums[l] < nums[r]:
                res = min(res,nums[l])
                break
            
            m = (l+r)//2
            res = min(res,nums[m])
            if nums[m] >= nums[l]:
                # go right
                l = m + 1
            else:
                r = m - 1
        
        return res

        
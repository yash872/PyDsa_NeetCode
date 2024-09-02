# Two Integer Sum II - LeetCode 167

# AS a bruteforce solution we can check every 2 num cobination which willl take Tx-> O(n^2)


# we will take 2 pointers from left and right
# as the array is sorted, move left pointer if sum is less than target 
# move right if sum is more than target
# Tx-> O(n)

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            curSum = numbers[l] + numbers[r]

            if curSum > target:
                r -= 1
            elif curSum < target:
                l += 1
            else:
                return [l + 1, r + 1]
        
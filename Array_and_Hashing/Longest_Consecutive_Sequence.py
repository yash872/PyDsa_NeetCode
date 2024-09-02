# Logest Consecutive Sequence - LeetCode 128


# we can sort the array and find out the Longest Consecutive Sequence but Tx-> O(nlogn)


# we will cast the list into set, and check for the n-1 element in set, if not exist n is the start of sequence.
# if we find start of any sequence, we will look for consecutive numbers and trake the length
# return the max length, Tx-> (n), Sx-> O(n)

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for n in numSet:
            if (n - 1) not in numSet:
                length = 1
                while (n + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest

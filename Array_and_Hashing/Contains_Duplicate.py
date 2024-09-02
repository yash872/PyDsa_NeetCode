# Contains Duplicate - LeetCode 217


# we can sort and iterate with 2 pointer one after another to check duplicate, T-> (nlonn)

# we will keep value in hashset and check if already exist, Tx-> n , Sx-> n
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False

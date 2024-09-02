# Valid Anagram - LeetCode 242


# sort them and compare, tx-> O(nlogn)

# create 2 dict to store each character count and compare, Tx-> O(s+t), Sx-> O(s+t)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT
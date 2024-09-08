# LeetCode - 424

# Bruteforce to check all combination, O(n^2)

# we will create a charMap to store char and their index
# if a char repeat, we will check it is in the current substring
# if Yes then we will update the index in charMap and shift the start
# record the current substring len if max.
# Tx-> O(n)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charMap = {}
        maxLength = 0
        start = 0

        for i,c in enumerate(s):
            if c in charMap:
                if charMap[c] >= start:
                    # means the char is part of the current substring
                    # shift the start point to the next of that char position 
                    start = charMap[c]+1
            maxLength = max(maxLength,i-start+1)
            charMap[c] = i
        
        return maxLength

        
# Leetcode - 3

# Bruteforce will have all possible combination, O(n^2)

# we will create a window and also count the freq of every char in dict
# we will check how many char we have to replace, which should be <k
# window length - maxFreq char should be < k
# if above condition not true, then we will shift left pointer
# and reduce the count of that char
# while removing left char we are not updating the maxFreq 
# as it wont affect our end res, as decrease in maxFreq not increase res
# so just leave it, and it will avoid to check maxFreq in charMap so no O(26)
# final Tx-> O(n)

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charMap = {}
        res = 0

        l = 0
        maxFreq = 0

        for r in range(len(s)):
            charMap[s[r]] = 1 + charMap.get(s[r], 0)
            maxFreq = max(maxFreq, charMap[s[r]])

            while ((r-l+1) - maxFreq > k):
                charMap[s[l]] -=1
                l+=1
            res = max(res, (r-l+1))
        
        return res

        


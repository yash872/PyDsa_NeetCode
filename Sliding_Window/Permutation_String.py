# LeetCode - 567

# Brute Force is to check all possible permutaion in the string, Tx-> O(n^2)

# Optimized Approch:
# create hashmap of the first string, and the S1 length window of 2nd string
# compare if they same return True as False
# Tx-> O(26*n), Sx-> O(n) 
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False

        s1Map = {}
        s2Map = {}

        for i in range(len(s1)):
            s1Map[s1[i]] = 1 + s1Map.get(s1[i],0)
        
        left = 0
        right = 0
        wn = len(s1)

        while right<len(s2):
            if (right - left + 1) <= wn:
                s2Map[s2[right]] = 1 + s2Map.get(s2[right],0)
                right+=1
                if s1Map == s2Map:
                    return True
            else:
                s2Map[s2[left]] -=1
                if s2Map[s2[left]] == 0:
                    s2Map.pop(s2[left])
                left+=1
        
        return False
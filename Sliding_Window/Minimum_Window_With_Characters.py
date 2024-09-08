# LeetCode - 76

# Tx-> O(n)
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        
        if len(s) < len(t):
            return ""
        
        charMap = {}
        for ch in t:
            charMap[ch] = 1 + charMap.get(ch,0)
        
        minLen = float('inf')
        tlen = len(t)
        start = -1
        left = 0
        right = 0
        count = 0 # required sub string count

        while right < len(s):
            # if the ch already present in charMap
            if s[right] in charMap:
                if(charMap[s[right]]>0):
                    count +=1
            charMap[s[right]] = charMap.get(s[right],0) - 1


            while(count == tlen):
                # update min window
                if(right-left+1 < minLen):
                    minLen = right-left+1
                    start = left
                
                # removal from left
                charMap[s[left]] +=1
                if (charMap[s[left]]>0):
                    count-=1
                left+=1
            
            right+=1

        if start == -1:
            return ""
        else:
            return s[start:start+minLen]
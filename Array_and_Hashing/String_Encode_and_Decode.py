# String Encode and Decode - LeetCode 271

# we can encode and decode it with any of our logic but we will have to be cautious if the delimeter
# appears in betwen word. so we will have lent of each word and concate the len and the word with '#'
# so ['Yash', 'bhawsar'] will become '4#Yash7#Bhawsar' as ecoded string
# Tx-> O(n) where n is total number of character in the input

class Solution:
    
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j
            
        return res

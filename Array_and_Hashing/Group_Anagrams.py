# Groups Anagrams - LeetCode 49

# sort all the strings and group them by compare will take Tx-> m*(nlogn)

# for every character of each string, we will create a count list having character counts 
# of that string, we use that count list as Key converting as Tuple coz list can't be Key
# and add those strings as values for that key, and return 
# all the values at the end which is list of list of grouped strings
# Tx-> O(m*n*26) which is similar to O(m*n)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            ans[tuple(count)].append(s)
        return ans.values()
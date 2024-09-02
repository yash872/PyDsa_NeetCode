# Top K Elements in List

# create a frequency map and sort it on counts to get top K, Tx-> O(nlogn)

# create frequency map
# create list of lists len n+1, and store number considering occurence as index,
# iterate from back to get top K, return in list
# Tx-> O(n), Sx-> O(n)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
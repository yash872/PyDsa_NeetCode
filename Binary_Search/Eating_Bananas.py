# Brute Force is to check with all possible value of K whic will be from 1 to max(piles)
# Tx->O(max(piles)*n)


# for same possible values of K, 1 to Max(piles)
# we will perform binary search on that find the number in logn
# Tx-> O(log(max(piles)))
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l <= r:
            k = (l + r) // 2

            totalTime = 0
            for p in piles:
                totalTime += math.ceil(float(p) / k)
            if totalTime <= h:
                res = k
                r = k - 1
            else:
                l = k + 1
        return res

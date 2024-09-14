# LeetCode - 739

# we will keep the temp and indx in a stack for every element and pop it 
# if someone greater than that comes after it, take the indx diff and put it in result
# Tx-> O(n)

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] # pair: [temp, index]

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = (i - stackInd)
            stack.append([t, i])

        return res        
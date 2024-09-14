# Brute for is to travel all cells, Tx-> O(m*n)

# you can perform binary search on all rows, Tx-> O(m*logn)

# we will first find the correct row, and then check that row with bianry search
# Tx-> O(logm + logn) => O(logm*n)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows,cols = len(matrix),len(matrix[0])
        
        # we will search the correct row 
        low, high = 0, rows - 1
        while low <= high:
            row = low + (high - low)//2
            if target > matrix[row][-1]:
                low = row + 1
            elif target < matrix[row][0]:
                high = row - 1
            else:
                break

        # if no correct wor and while condition failed
        if not (low <= high):
            return False
        
        row = low + (high - low)//2
        l,r = 0, cols-1
        while l <= r:
            m = l + (r-l)//2
            print(m)
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True
        
        return False

        
import math

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m,n = len(matrix), len(matrix[0])
        l, r = 0, m-1
        while l != r:
            mid=math.ceil((l+r)/2)
            if matrix[mid][0] > target:
                r = mid-1
            else:
                l = mid
        if matrix[l][0] == target:
            return True
        x=l
        l,r = 0, n-1
        while l != r:
            mid=math.ceil((l+r)/2)
            if matrix[x][mid] > target:
                r = mid-1
            else:
                l = mid
        if matrix[x][l] == target:
            return True
        return False

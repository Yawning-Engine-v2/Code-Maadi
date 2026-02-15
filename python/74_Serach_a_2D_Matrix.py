from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i,j = 0,0
        while i < len(matrix):
            if target > matrix[i][len(matrix[i])-1]:
                i += 1
            else:
                if target in matrix[i]:
                    return True
                else:
                    return False
        return False
    # This is o(m+n)
    # change the target in matrix[i] to binary search
    # time complexity becomes o(m = log(n))
    # instead of incrementing the outer loop by one
    # use binary search with the first element to get
    # o(log(m) + log(n))
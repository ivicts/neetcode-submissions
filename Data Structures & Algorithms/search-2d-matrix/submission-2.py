class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        m = len(matrix)
        n = len(matrix[0])

        l, r = 0, m*n - 1

        while (l <= r):
            mid = l + ((r - l))//2
            i = mid//n
            j = mid % n
            #print(l, mid, r, i, j)
            if matrix[i][j] < target:
                l = mid + 1
            elif matrix[i][j] > target:
                r = mid - 1
            elif matrix[i][j] == target:
                return True

        return False
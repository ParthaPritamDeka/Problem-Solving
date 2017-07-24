matrix =[
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
class Solution:
    # @param matrix, a list of lists of integers
    # @param target, an integer
    # @return a boolean
    # 8:21
    def searchMatrix(self, matrix, target):
        if not matrix or target is None:
            return False

        rows, cols = len(matrix), len(matrix[0])
        low, high = 0, rows * cols - 1
        #0,11
        
        while low <= high:
            mid = (low + high) / 2
            #5
            num = matrix[mid / cols][mid % cols]
            #matrix(2)[1]

            if num == target:
                return True
            elif num < target:
                low = mid + 1
            else:
                high = mid - 1
        
        return False

a = Solution()
b = a.searchMatrix(matrix, 3)
print b 

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        row = 0
        # start at the top right corner
        col = len(matrix[0]) - 1

        while row < len(matrix) and col >= 0:
            # first prints 7 in example shown
            val = matrix[row][col]

            if val == target:
                return True
            elif val > target:
                # Move left
                col -= 1
            else:
                # Move down
                row += 1
        return False

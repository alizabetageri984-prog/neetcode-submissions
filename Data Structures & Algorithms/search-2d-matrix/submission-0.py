class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        cols= len(matrix[0])

        left_pointer = 0 
        right_pointer = row * cols - 1

        while left_pointer <= right_pointer:
            mid = (left_pointer + right_pointer) // 2

            row =mid // cols
            col = mid % cols

            if matrix[row][col] == target:
                return True

            elif matrix[row][col] < target:
                left_pointer = mid + 1

            else:
                right_pointer = mid - 1

        return False
        
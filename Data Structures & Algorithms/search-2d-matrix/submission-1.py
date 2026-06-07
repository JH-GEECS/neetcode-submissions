class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        log(m) + log(n)

        """
        row_left_idx = 0
        row_right_idx = len(matrix)-1
        target_row_idx = 0

        while row_left_idx <= row_right_idx:
            row_mid_idx = (row_left_idx + row_right_idx) // 2

            if matrix[row_mid_idx][0] <= target:
                target_row_idx = row_mid_idx
                row_left_idx = row_mid_idx + 1
            else:
                row_right_idx = row_mid_idx - 1

        column_left_idx = 0
        column_right_idx = len(matrix[0])-1
        target_column_idx = 0

        while column_left_idx <= column_right_idx:
            column_mid_idx = (column_right_idx + column_left_idx) // 2

            if matrix[target_row_idx][column_mid_idx] <= target:
                if matrix[target_row_idx][column_mid_idx] == target:
                    target_column_idx = column_mid_idx

                column_left_idx = column_mid_idx + 1
            else:
                column_right_idx = column_mid_idx - 1

        if matrix[target_row_idx][target_column_idx] == target:
            return True
        else:
            return False


            




        
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        pass

        from collections import Counter
        # row_check
        row_valid = True
        for i in range(len(board)):
            each_row = Counter(board[i])

            for key, val in each_row.items():
                if key != "." and val >= 2:
                    row_valid = False
                    break
        # column check
        column_valid = True
        for i in range(len(board[0])):
            _each_col = [board[j][i] for j in range(len(board))]
            each_col = Counter(_each_col)

            for key, val in each_col.items():
                if key != "." and val >= 2:
                    column_valid = False
                    break

        # square valid
        """
        [0,0], [0,1], [0,2]
        [1,0], [1,1], [1,2]
        [2,0], [2,1], [2,2]
        """

        square_valid = True
        from itertools import product
        for i in range(0, len(board), 3):
            for j in range(0, len(board[0]), 3):
                _each_square = [
                    board[k+i][l+j] for k, l in product(range(3), range(3))
                ]
                each_square = Counter(_each_square)

                for key, val in each_square.items():
                    if key != "." and val >= 2:
                        square_valid = False
                        break

        if row_valid and column_valid and square_valid:
            return True
        else:
            return False
        
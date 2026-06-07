class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        from collections import Counter

        def valid_checker(elems: List):
            elem_count = Counter(elems)
            for k, v in elem_count.items():
                if k != "." and v >=2:
                    return False

            return True

        # row_check
        for i in range(len(board)):
            if not valid_checker(board[i]):
                return False

        # column check
        for i in range(len(board[0])):
            _each_col = [board[j][i] for j in range(len(board))]
            if not valid_checker(_each_col):
                return False

        # square valid
        from itertools import product
        for i, j in product(range(0, len(board), 3), range(0, len(board[0]), 3)):
            _each_square = [
                board[k+i][l+j] for k, l in product(range(3), range(3))
            ]
            if not valid_checker(_each_square):
                return False

        return True
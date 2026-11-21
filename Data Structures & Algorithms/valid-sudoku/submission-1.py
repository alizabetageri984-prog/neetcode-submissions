class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        box = [set() for _ in range(9)]
        
        for r in range(9):
            for c in range(9):

                num= board[r][c]

                if num ==".":
                    continue

                box_index = (r // 3) * 3 + (c // 3)

                if(num in row[r] or num in cols[c] or num in box[box_index]):
                    return False

                row[r].add(num)
                cols[c].add(num)
                box[box_index].add(num)
        return True
from typing import List, Dict
from collections import defaultdict, Counter
from functools import reduce


# multiply = reduce((lambda x, y: x*y), lst)

def valid_sudoku(sudoku: List[List[str]]) -> bool:

    #print(sudoku)
    unique = set()

    # column
    for i in range(0, 9):

        unique = set()
        for j in range(0, 9):
            
            cell = sudoku[i][j]
            # Checking is the cell is not "." and not in set
            if cell != 0 and cell in unique:
                return False
            # Appending every cells into a set to get unique elements
            unique.add(cell)

    # row
    for i in range(0, 9):

        unique = set()
        for j in range(0, 9):
            cell = sudoku[i][j]
            if cell != 0 and cell in unique:
                return False
            unique.add(cell)

    #each sub region
    for row in range(0, 9, 3):
        for col in range(0, 9, 3):
            
            # Start of each sub region 3x3
            unique = set()
            
            # Iterating over that sub region
            for i in range(row, row+3):
                for j in range(col, col+3):
                    cell = sudoku[i][j]
                    if cell != 0 and cell in unique:
                        return False
                    unique.add(cell)

    return True

# More optimized code

def valid_sudoku_opt(sudoku: List[List[str]]) -> bool:

    res = []
    for r, row in enumerate(sudoku):
        for c, cell in enumerate(row):
            if cell != 0:
                res += [(r, cell), (cell, c), (r // 3, c // 3, cell)]

    return len(res) == len(set(res))

def isValidSudoku(board):
    res = []
    for i in range(9):
        for j in range(9):
            element = board[i][j]
            if element != 0:
                res += [(i, element), (element, j), (i // 3, j // 3, element)]
    return len(res) == len(set(res))

if __name__ == "__main__":
    # sudoku = [[int(cell) for cell in input().split()] for _ in range(9)]

    board = [["5","3",".",".","7",".",".",".","."]
            ,["6",".",".","1","9","5",".",".","."]
            ,[".","9","8",".",".",".",".","6","."]
            ,["8",".",".",".","6",".",".",".","3"]
            ,["4",".",".","8",".","3",".",".","1"]
            ,["7",".",".",".","2",".",".",".","6"]
            ,[".","6",".",".",".",".","2","8","."]
            ,[".",".",".","4","1","9",".",".","5"]
            ,[".",".",".",".","8",".",".","7","9"]]

    board2 = [
        ["8","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]
    ]

    converted_board = [[int(cell) if cell != "." else 0 for cell in row] for row in board]

    print(valid_sudoku(converted_board))
    print(valid_sudoku_opt(converted_board))
    print(isValidSudoku(converted_board))
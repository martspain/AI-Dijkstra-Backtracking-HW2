# TODO
from operator import ne


class Sudoku:
    def __init__(self, count, restrictions):
        self.sudokuCount = count
        self.restrictions = restrictions
        self.board = []
        self.createBoard()
    
    def createBoard(self):
        for i in range(self.sudokuCount):
            row = []
            for j in range(self.sudokuCount):
                row.append(0)
            self.board.append(row)
    
    def addRestriction(self, x, y, n):
        self.board[x][y] = n

    def showRawSudoku(self):
        print("Sudoku Board:")
        for i in self.board:
            print(i)

    def solver(self):
        pass
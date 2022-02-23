# TODO
from operator import ne

squareSize = 3

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

    '''
    fuentes consultadas/utilizadas para el algoritmo de backtracking:
    https://www.geeksforgeeks.org/sudoku-backtracking-7/
    https://www.geeksforgeeks.org/backtracking-algorithms/
    https://medium.com/daily-python/solving-sudoku-puzzle-using-backtracking-in-python-daily-python-29-99a825042e
    '''
    def findEmpty(self, arr, l):
        for row in range(len(self.board)):
            for col in range(len(self.board[0])):
                if(arr[row][col]== 0):
                    l[0]= row
                    l[1]= col
                    return True
            return False
    
    def usedInRow(self, arr, row, num):
        for i in range(len(self.board)):
            if(arr[row][i] == num):
                return True
        return False

    def usedInCol(self, arr, col, num):
        for i in range(len(self.board[0])):
            if(arr[i][col] == num):
                return True
        return False
    
    def usedInBox(self, arr, row, col, num):
        global squareSize
        for i in range(squareSize):
            for j in range(squareSize):
                if(arr[i + row][j + col] == num):
                    return True

    def checkLocationIsSafe(self, arr, row, col, num):
        global squareSize
        return not self.usedInRow(arr, row, num) and not self.usedInCol(arr, col, num) and not self.usedInBox(arr, row - row % squareSize, col - col % squareSize, num)

    def solveSudoku(self):
        l =[0, 0]
        if(not self.findEmpty(self.board, l)):
            return True

        row, col = l

        for num in range(1, self.sudokuCount + 1):
            if(self.checkLocationIsSafe(self.board, row, col, num)):
                self.board[row][col] = num
                if(self.solveSudoku()):
                    return True
                self.board[row][col] = 0
        return False


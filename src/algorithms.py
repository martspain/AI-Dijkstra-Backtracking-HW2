# Dijkstra algorithm implementation
import heapq

'''
Sources seen for the implementation of this Dijkstra's algorithm.:
Pseudocode from this page
https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm
''' 

# This Dijkstra Algorithm finds the shortest path for a directed graph given the graph itself, a start node and an end node.
def dijkstra(g, startNode, endNode):
    infinity = 10000000000

    # Stores distance of each vertex from source vertex
    q = [ (infinity, node)  for node in g.vertices]
    distances = {node: infinity for node in g.vertices}
   
    path = { v : None for v in g.vertices }
    q[startNode -1] = (0, startNode)
    distances[startNode] = 0
    heapq.heapify(q)
       
    while len(q):
        # Mark current as visited
        d,  current = heapq.heappop(q)
       
        for nbr in g.vertices[current]:
            v, w = nbr[0], nbr[1]
           
            dist = d + w
            if dist < distances[v]:
                distances[v] = dist
                path[v] = current
                heapq.heappush( q, (distances[v] , v) )
                if v == endNode:
                    result = [ endNode ]
                    parent = path[v]
                    while parent:
                        result.append(parent)
                        parent = path[parent]
                    return result[::-1], distances[endNode]



#backtracking implementation 
'''
fuentes consultadas/utilizadas para el algoritmo de backtracking:
https://www.geeksforgeeks.org/sudoku-backtracking-7/
https://www.geeksforgeeks.org/backtracking-algorithms/
https://medium.com/daily-python/solving-sudoku-puzzle-using-backtracking-in-python-daily-python-29-99a825042e
''' 

# A Backtracking program to solve Sudoku

def findEmpty(arr, l):
    for row in range(len(arr)):
        for col in range(len(arr[row])):
            if(arr[row][col]== 0):
                l[0]= row
                l[1]= col
                return True
        return False
    
def usedInRow(arr, row, num):
    for i in range(len(arr)):
        if(num == arr[row][i]):
            return False
    return True

def usedInCol(arr, col, num):
    for i in range(len(arr)):
        if(num == arr[i][col]):
            return False
    return True
    
def usedInBox(arr, row, col, num):
    r=(row//3)*3+1
    c=(col//3)*3+1
    for i in [-1,0,1]:
        for j in [-1,0,1]:
            if arr[r+i][c+j]==num:
                return False
    return True

def findUnassigned(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if(arr[i][j] == 0):
                return i, j
    return -1, -1

def checkLocationIsSafe(arr, row, col, num):
    global squareSize
    return not usedInRow(arr, row, num) and not usedInCol(arr, col, num) and not usedInBox(arr, row - row % squareSize, col - col % squareSize, num)

def solveSudoku(arr):
    i, j = findUnassigned(arr)
    if(i == -1 and j == -1):
        return True
    
    for num in range(1,10):
        if usedInRow(arr, i, num) and usedInCol(arr, j, num) and usedInBox(arr, i, j, num):
            arr[i][j] = num

            if solveSudoku(arr):
                return True

            arr[i][j] = 0
    return False
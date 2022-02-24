# Dijkstra algorithm implementation
from vertex import Vertex
from graph import Graph

def dijkstra(G, startNode, endNode):
    infi = 10000000000
    # Stores distance of each
    # vertex from source vertex
    path = [0 for i in range(len(G.nodes))]
    dist = [infi for i in range(len(G.nodes))]
   
    # bool array that shows
    # whether the vertex 'i'
    # is visited or not
    visited = [False for i in range(len(G.nodes))]
     
    for i in range(len(G.nodes)):       
        path[i] = -1
    dist[startNode] = 0
    path[startNode] = -1
    current = startNode
   
    # Set of vertices that has
    # a parent (one or more)
    # marked as visited
    sett = set()    
    while (True):
           
        # Mark current as visited
        visited[current] = True
        for i in range(len(Vertex.getRelatedNodes(current))): 
            w = Graph.getNodeEdges(current) 
            v = w[0]         
            if (visited[v]):
                continue
   
            # Inserting into the
            # visited vertex
            sett.add(v)
            alt = dist[current] + w[1]
   
            # Condition to check the distance
            # is correct and update it
            # if it is minimum from the previous
            # computed distance
            if (alt < dist[v]):      
                dist[v] = alt
                path[v] = current;       
        if current in sett:           
            sett.remove(current);       
        if (len(sett) == 0):
            break
   
        # The new current
        minDist = infi
        index = 0
   
        # Loop to update the distance
        # of the vertices of the graph
        for a in sett:       
            if (dist[a] < minDist):          
                minDist = dist[a]
                index = a;          
        current = index;  
    return dist


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
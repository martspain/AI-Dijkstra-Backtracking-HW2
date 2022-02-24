# Dijkstra algorithm implementation
from vertex import Vertex
from graph import Graph

def dijkstra(G, startNode, endNode):
    infinity = 10000000000

    #Create the path
    path = [0 for i in range(len(G.nodes))]

    # Stores distance of each vertex from source vertex
    distance = [infinity for i in range(len(G.nodes))]
   
    # This list shows wheter the vertex is visited or not.
    unseen = [False for i in range(len(G.nodes))]
     
    for i in range(len(G.nodes)):       
        path[i] = -1
    distance[startNode] = 0
    path[startNode] = -1
    current = startNode
   
    # Set of vertices that has a parent marked as visited
    sett = set()    
    while (True):
           
        # Mark current as visited
        unseen[current] = True

        for i in range(len(G.nodes[current].reachable)): 
            print('this is the reachable ====>',G.nodes[current].reachable)
            w = G.nodes[current].reachable[i]  #Graph.getNodeEdges(G, current) G.nodes[current].reachable[i]
            print('this is w ===>', w)
            x = Graph.getNodeEdges(G, w)
            print('this is the node edges =====>',x)
            for edge in range(len(x)):
                v = edge.origin.value
            print('this is origin ====>',v)
            if (unseen[v]):
                continue
   
            #inserting into visited vertex    
            sett.add(v)
            for i in range(len(x)):
                u = i.destination
            print('this is destination ====>', u)
            alt = distance[current] + u
   
            # This condition check if the distance is correct and then updated it
            if (alt < distance[v]):      
                distance[v] = alt
                path[v] = current;       
        if current in sett:           
            sett.remove(current);       
        if (len(sett) == 0):
            break
   
        minDistance = infinity
        index = 0
   
        # this loop updates the distance of the vertices in the graph
        for a in sett:       
            if (distance[a] < minDistance):          
                minDistance = distance[a]
                index = a;          
        current = index;  
    return distance


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
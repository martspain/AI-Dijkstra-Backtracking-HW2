''' 
Universidad del Valle de Guatemala
Inteligencia Artificial - Sección 20
Autores:
    Martín España   Carné: 19258
    Diego Arredondo Carné: 19422
    Alejandra Gudiel Carné: 19232
'''

from fileReader import FileReader
from fileWriter import FileWriter
from algorithms import dijkstra, solveSudoku
import algorithms as alg
from pprint import pprint


class Graph:
    def __init__(self):
        self.vertices = {}
       

    def read_graph(self, filename):
        with open(filename) as fp:
            for line in fp:
                line = line.strip()
                if line :
                    v, u, w = line.split(" ")
                    edges = self.vertices.get(int(v))     
                    if not edges:
                        edges = []
                        self.vertices[int(v)] = edges
                    edges.append( (int(u),int(w)) )

                    if int(u) not in self.vertices:
                        self.vertices[int(u)] = []

    def print(self):
        for node, edges in self.vertices.items():
            for edge in edges:
                print(node, "=>", edge[0] , " peso ", edge[1])


# TODO Change this to True when program is finished
showBanner = False
if showBanner:
    # Print banner
    print('|||      |||  \\\            ///  ||||||||||||')
    print('|||      |||   \\\          ///   |||')
    print('|||      |||    \\\        ///    |||')
    print('|||      |||     \\\      ///     |||  |||||||')
    print('|||      |||      \\\    ///      |||      |||')
    print('|||      |||       \\\  ///       |||      |||')
    print('||||||||||||        \\\///        ||||||||||||')
    print('-----------------------------------')
    print('Universidad del Valle de Guatemala')
    print('Inteligencia Artificial - Sección 20')
    print('Autores:')
    print('     Martín España     Carné: 19258')
    print('     Diego Arredondo   Carné: 19422')
    print('     Alejandra Gudiel  Carné: 19232')
    print('Fecha: 24-02-2022')
    print('Versión: 1.0')
    print('----------------------------------- \n')

opcionMenu = 0
while opcionMenu != 3:
    print('1. Probar el algoritmo de Dijkstra \n2. Probar el backtracking con sudoku \n3. Salir\n')

    opcionMenu = int(input('Ingrese una opción: '))
    
    if opcionMenu == 1:
        #PARA EL GRAFO
        # Read input file for graph
        g = Graph()
        g.read_graph("input.txt")
        print("Graph")
        g.print()
        startNode = int(input('Ingrese el nodo donde quiere comenzar el recorrido: '))
        endNode = int(input('Ingrese el nodo donde quiere terminar el recorrido: '))
        path = dijkstra(g, startNode, endNode)
        print("Dijkstra camino mas corto (nodos, peso total):", path)
        #g.getShortestPath(1,7)

        # Write output to the corresponding output file
        w = FileWriter('output.txt')

        w.writeIterableOutput('Shortest Path From 1 to 7', [(1,2,3), (2,5,6), (5,7,2)])
        w.appendOutput('Path Weight: 11')

    if opcionMenu == 2:
        #PARA EL SUDOKU
        # Read input file for sudoku
        print('\nLos sudokus disponibles: \n1. 4x4 \n2. 6x6 \n3. 9x9 \n4. Salir\n')
        opcionS = int(input('\nIngrese el número de sudoku que desee resolver: '))

        if opcionS == 1:
            # Read input file for sudoku
            rs = FileReader('sudoku4.txt')
            # Create a sudoku board
            s = rs.createSudoku('sudoku4.txt')
            # Show current sudoku
            s.showRawSudoku()
            puzzle = s.getPuzzle()
            print('\n-----------------------')
            solved = alg.solveSudoku(puzzle, 4)
            if(solved == True):
                print("Solved Sudoku")
                for n in puzzle:
                    pprint(n)
                print('\n-----------------------')
                
            else:
                print("Unsolvable Sudoku")
            

        if opcionS == 2:
            # Read input file for sudoku
            rs = FileReader('sudoku6.txt')
            # Create a sudoku board
            s = rs.createSudoku('sudoku6.txt')
            # Show current sudoku
            s.showRawSudoku()
            puzzle = s.getPuzzle()
            print('\n-----------------------')
            solved = alg.solveSudoku(puzzle, 6)
            if(solved == True):
                print("Solved Sudoku")
                pprint(puzzle)
                print('\n-----------------------')
                
            else:
                print("Unsolvable Sudoku")

        if opcionS == 3:
            # Read input file for sudoku
            rs = FileReader('sudoku9.txt')
            # Create a sudoku board
            s = rs.createSudoku('sudoku9.txt')
            # Show current sudoku
            s.showRawSudoku()
            puzzle = s.getPuzzle()
            print('\n-----------------------')
            solved = alg.solveSudoku(puzzle, 9)
            if(solved == True):
                print("Solved Sudoku")
                pprint(puzzle)
                print('\n-----------------------')
                
            else:
                print("Unsolvable Sudoku")

        else: 
            print('\nSaliendo del sudoku...')

    else:
        print('Saliendo...')
        break

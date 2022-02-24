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
        rg = FileReader('input.txt')
        # Create a directed graph from file
        g = rg.createGraph('Graph One', True)
        # Show current graph
        g.showRawGraph()

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
            # Solve sudoku
            s.solveSudoku()

        if opcionS == 2:
            # Read input file for sudoku
            rs = FileReader('sudoku6.txt')
            # Create a sudoku board
            s = rs.createSudoku('sudoku6.txt')
            # Show current sudoku
            s.showRawSudoku()
            # Solve sudoku
            s.solveSudoku()

        if opcionS == 3:
            # Read input file for sudoku
            rs = FileReader('sudoku9.txt')
            # Create a sudoku board
            s = rs.createSudoku('sudoku9.txt')
            # Show current sudoku
            s.showRawSudoku()
            # Solve sudoku
            s.solveSudoku()

        else: 
            print('\nSaliendo del sudoku...')

    else:
        print('Saliendo...')
        break

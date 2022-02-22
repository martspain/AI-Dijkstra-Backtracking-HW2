''' 
Universidad del Valle de Guatemala
Inteligencia Artificial - Sección 20
Autores:
    Martín España   Carné: 19258
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
    print('     Martín España   Carné: 19258')
    print('     Diego Arredondo   Carné: 19422')
    print('Fecha: 24-02-2022')
    print('Versión: 1.0')
    print('----------------------------------- \n')

#PARA EL GRAFO
# Read input file for graph
rg = FileReader('input.txt')
# Create a directed graph from file
g = rg.createGraph('Graph One', True)
# Show current graph
g.showRawGraph()

#PARA EL SUDOKU
# Read input file for sudoku
rs = FileReader('sudoku6.txt')
# Create a sudoku board
s = rs.createSudoku('sudoku9.txt')
# Show current sudoku
s.showRawSudoku()

# Write output to the corresponding output file
w = FileWriter('output.txt')

w.writeIterableOutput('Shortest Path From 1 to 7', [(1,2,3), (2,5,6), (5,7,2)])
w.appendOutput('Path Weight: 11')

from graph import Graph
from sudoku import Sudoku

class FileReader:
    def __init__(self, address):
        self.directory = address
        self.nodeCount = 0
        self.edgeCount = 0
        self.edges = []
        self.fileContent = []
        self.readFile()
    
    def readFile(self):
        try:
            with open(self.directory, 'r') as file:
                fileEdges = file.readlines()
            # Cleanup the input buffer
            for line in fileEdges:
                if line != '\n' and line != ' ' and line != '' and line[0] != '#':
                    self.fileContent.append(line.replace('\n', ''))
            
            try:
                self.nodeCount = int(self.fileContent.pop(0))
                self.edgeCount = int(self.fileContent.pop(0))
            except ValueError:
                print('\n#############################################################################################')
                print('Error: Check that Node Count and Edge Count are correctly written in "' + self.directory + '"')
                print('#############################################################################################')
        except FileNotFoundError:
            print('\n#############################################')
            print('Error: File "' + self.directory + '" not found.')
            print('#############################################')
    
    def createGraph(self, name, directional):
        newGraph = Graph(name, directional)

        try:
            # Add graph's nodes
            for i in range(self.nodeCount):
                newGraph.createNode(i+1)

            # Add graph's edges
            for edge in self.fileContent:
                data = edge.split(' ')
                dataOrig = int(data[0])
                dataDest = int(data[1])
                dataWeight = int(data[2])

                if dataOrig >= 1 and dataDest >= 1 and dataWeight >= 0:
                    newGraph.createEdge(dataOrig, dataDest, dataWeight)
                elif dataOrig >= 1 and dataDest >= 1 and dataWeight < 0:
                    print('\n#######################################################')
                    print('Error: Edge\'s weight must be greater than or equal to 0.')
                    print('#######################################################')
                elif (dataOrig < 1 or dataDest < 1) and dataWeight >= 0:
                    print('\n############################################################')
                    print('Error: Node value must be a number greater than or equal to 1')
                    print('############################################################')

        except ValueError:
            print('\n#########################################################################')
            print('Error: Check the edges data is correctly written in "' + self.directory +'"')
            print('#########################################################################')
        
        return newGraph
    
    # TODO
    def createSudoku(self):
        return Sudoku(4)
        
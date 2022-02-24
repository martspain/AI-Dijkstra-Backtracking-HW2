from vertex import Vertex
from edge import Edge
#from algorithms import dijkstra

class Graph:
    def __init__(self, name, directional = False):
        self.name = name
        self.nodes = []
        self.edges = []
        self.directional = directional
    
    # Create node
    def createNode(self, nodeVal):
        self.nodes.append(Vertex(nodeVal))
    
    # Create edge from existing nodes
    def createEdge(self, firstVal, secondVal, weight):
        originNode = -1
        destinyNode = -1

        # Search for the Nodes to create the edge
        for node in self.nodes:
            if node.value == firstVal:
                originNode = node
            elif node.value == secondVal:
                destinyNode = node
        
        if originNode != -1 and destinyNode != -1:
            # If is directed graph then the only relation is A -> B
            originNode.createRelation(destinyNode)
            # Else the relation is from both sides A <-> B
            if not self.directional:
                destinyNode.createRelation(originNode)

            # Add the resulting edge to the graph's collection
            self.edges.append(Edge(originNode, destinyNode, weight, self.directional))
        else:
            print('\n#############################')
            print('Error 404')
            print('#############################')
            if originNode == -1:
                print('Origin Node not found in collection.')
            if destinyNode == -1:
                print('Destiny Node not found in collection.')
            print('\n')
    
    # Get all edges where nodeVal exists
    def getNodeEdges(self, nodeVal):
        result = []
        if self.directional:
            # Only A --> B ... being nodeVal = A ... origin
            for edge in self.edges:
                if edge.origin == nodeVal:
                    result.append(edge)

        elif not self.directional:
            # A <--> B
            for edge in self.edges:
                if edge.origin == nodeVal or edge.destiny == nodeVal:
                    result.append(edge)
        
        return result

    # Gets a path from start node to end node
    def getPath(self, start, end):
        temp = []
        for edge in self.edges:
            temp.append(edge.raw)
        return temp

    # Gets all posible paths from start node to end node
    def getAllPaths(self, start, end):
        temp = [(start, end, 0)]
        return temp

    # Gets the shortest path using Dijkstra algorithm
   # def getShortestPath(self, start, end):
    #    return dijkstra(self, start, end)

    # Return edges
    def getEdges(self):
        return self.edges
    
    # Return nodes
    def getNodes(self):
        return self.nodes
    
    # Return how many nodes exist in the graph
    def getNodesSize(self):
        return len(self.nodes)
    
    # Return how many edges exist in the graph
    def getEdgesSize(self):
        return len(self.edges)
    
    # Show the graph as a raw collection of edges
    def showRawGraph(self):
        connector = ' --> ' if self.directional else ' <--> '
        print('\n-------------------')
        print(self.name)
        print('-------------------')
        print('Node Count: ' + str(len(self.nodes)))
        print('Edge count: ' + str(len(self.edges)))
        print('-------------------')
        for elem in self.edges:
            print('(' + str(elem.origin.value) + ')' + connector + '(' + str(elem.destiny.value) + ')' + ' == ' + str(elem.weight))
        print('-------------------')

    # Show the graph as a collection of edges within a table
    def showGraph(self):
        print('\n-----------------------------')
        print(self.name)
        print('-----------------------------')
        print('Node Count: ' + str(len(self.nodes)))
        print('Edge count: ' + str(len(self.edges)))
        print('-----------------------------')
        print('| Origin | Destiny | Weight |')
        print('-----------------------------')
        for elem in self.edges:
            print('| ' + str(elem.origin.value) + '      | ' + str(elem.destiny.value) + '       | ' + str(elem.weight) + '      |')


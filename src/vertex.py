class Vertex:
    def __init__(self, value):
        # Node value
        self.value = value
        # Nodes to which this node is related (can reach from this node to them)
        self.reachable = []
    
    # Adds a related node
    def createRelation(self, relatedNode):
        self.reachable.append(relatedNode)
    
    # Returns related nodes
    def getRelatedNodes(self):
        return self.reachable

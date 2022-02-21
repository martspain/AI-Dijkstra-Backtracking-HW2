class Edge:
    def __init__(self, origin, destination, weight, directed = False):
        self.origin = origin
        self.destiny = destination
        self.weight = weight
        self.directed = directed
        self.raw = (origin.value, destination.value, weight)

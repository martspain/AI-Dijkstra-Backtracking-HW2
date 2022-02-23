# Dijkstra algorithm implementation
def dijkstra(G, startNode, endNode):
    result = []

    for edge in G.edges:
        result.append(edge.raw)
    
    return result


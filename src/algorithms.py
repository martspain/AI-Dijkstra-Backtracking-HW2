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



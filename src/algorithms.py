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



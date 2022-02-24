# Dijkstra algorithm implementation

def dijkstra(G, startNode, endNode):
    # empty dictionary to hold distances
    distances = {} 
    # list of vertices in path to current vertex
    predecessors = {} 
    
    # get all the nodes that need to be assessed
    to_assess = G.nodes

    # set all initial distances to infinity
    #  and no predecessor for any node
    for node in G.nodes:
        distances[node] = float('inf')
        predecessors[node] = None
    
    # set the initial collection of 
    # permanently labelled nodes to be empty
    sp_set = []

    # set the distance from the start node to be 0
    distances[startNode] = 0
    
    # as long as there are still nodes to assess:
    while len(sp_set) < len(to_assess):

        # chop out any nodes with a permanent label
        still_in = {node: distances[node]\
                    for node in [node for node in\
                    to_assess if node not in sp_set]}

        # find the closest node to the current node
        closest = min(still_in, key = distances.get)

        # and add it to the permanently labelled nodes
        sp_set.append(closest)
        
        # then for all the neighbours of 
        # the closest node (that was just added to
        # the permanent set)
        for node in G.nodes[closest]:
            # if a shorter path to that node can be found
            if distances[node] > distances[closest] +\
                       G.nodes[closest][node]:

                # update the distance with 
                # that shorter distance
                distances[node] = distances[closest] +\
                       G.nodes[closest][node]

                # set the predecessor for that node
                predecessors[node] = closest
                
    # once the loop is complete the final 
    # path needs to be calculated - this can
    # be done by backtracking through the predecessors
    path = [endNode]
    while startNode not in path:
        path.append(predecessors[path[-1]])
    
    # return the path in order start -> end, and it's cost
    return path[::-1], distances[endNode]



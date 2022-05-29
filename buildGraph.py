from graph import *
def build_graph(graphFileName, NodelocationsFileName ):
    graph = Graph()
    
    file = open(graphFileName, 'r')
    f = file.readlines()

    readEdges = []
    for line in f:
        readEdges.append(line.strip())
            
    for connection in readEdges:
        temp = connection.split(' ')
        if len(temp) == 3:
            edge = temp
            a = Node(edge[0])
            b = Node(edge[1])
            graph.add_edge(a, b, int(edge[2]))

        else:
            node = temp
            a = Node(node[0])
            graph.add_node(a)
    
    readNodes = []
    file = open(NodelocationsFileName, 'r')
    f = file.readlines()

    for line in f:
        line = (line.strip()).split(' ')
        readNodes.append(line[0])
        
    return (graph, readNodes)
    

from graph import Graph
from graph import Edge
from graph import Node
import time
from matplotlib import pyplot as plt


graph = Graph()

file = open('graph.txt', 'r')
f = file.readlines()

readEdges = []
for line in f:
    readEdges.append(line.strip())
        
# print(readEdges)

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
    


a = graph.verticies["Oradea"]
b = graph.verticies["Zerind"]


# ans = graph.dijkstra(a, b)
# print(ans)



readNodes = []

file = open('cityLocations.txt', 'r')
f = file.readlines()

for line in f:
    line = (line.strip()).split(' ')
    readNodes.append(line[0]) 
    
    
    
#To find the average time and pathlength using dfs



def evaluate(searchAlgorithm):
    counter = 0
    totalTimeTaken = 0
    totalPathLengths = 0
    
    for i in readNodes:
        for j in readNodes:
            a = graph.verticies[i]
            b = graph.verticies[j]
            if searchAlgorithm == 'dfs':
                start_time = time.time()
                path = graph.dfs(a,b)
                end_time = time.time()
            elif searchAlgorithm == 'bfs':
                start_time = time.time()
                path = graph.bfs(a,b)
                end_time = time.time()
            elif searchAlgorithm == 'dijkstra':
                start_time = time.time()
                path = graph.dijkstra(a,b)
                end_time = time.time()
                path = path[1]
            elif searchAlgorithm == 'astar':
                start_time = time.time()
                path = graph.astar(a,b)
                end_time = time.time()
                path = path[1]
                
            counter += 1
            timeTaken =  end_time - start_time
            totalTimeTaken += timeTaken
            totalPathLengths += len(path)

    averageTimeTaken = totalTimeTaken / counter
    averageSolutionLength = totalPathLengths / counter
    
    return (averageTimeTaken, averageSolutionLength)




# To find the average time and pathlength using dfs

resultForDfs = evaluate('dfs')
print(resultForDfs)

# #To find the average time and pathlength using bfs

resultForDfs = evaluate('bfs')
print(resultForDfs)

# To find the average time and pathlength using dijkstra

resultForDfs = evaluate('dijkstra')
print(resultForDfs)
# To find the average time and pathlength using dfs

resultForDfs = evaluate('astar')
print(resultForDfs)





# for iv, (k, v) in enumerate(m.verticies.items()):
#     print(v.name)

# for iv, (k, edge) in enumerate(m.edges.items()):
#     print(edge.right.name, edge.left.name, edge.weight)
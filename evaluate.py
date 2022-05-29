from buildGraph import *
import time

def evaluate(searchAlgorithm, graphFileName, NodeLocationsFileName  ):
    
    graph, readNodes = build_graph(graphFileName, NodeLocationsFileName)
    counter = 0
    totalTimeTaken = 0
    totalNodePathLengths = 0
    totalWeightPathLengths = 0
    
    for i in readNodes:
        for j in readNodes:
            a = graph.verticies[i]
            b = graph.verticies[j]
            if searchAlgorithm == 'dfs':
                start_time = time.time()
                path = graph.dfs(a,b)
                end_time = time.time()
                nodePath = path
                weightPath = 0
            elif searchAlgorithm == 'bfs':
                start_time = time.time()
                path = graph.bfs(a,b)
                end_time = time.time()
                nodePath = path
                weightPath = 0
            
            elif searchAlgorithm == 'dijkstra':
                start_time = time.time()
                path = graph.dijkstra(a, b)
                end_time = time.time()
                nodePath = path[1]
                weightPath = path[0]
            
            elif searchAlgorithm == 'astar':
                start_time = time.time()
                path = graph.astar(NodeLocationsFileName,a,b)
                end_time = time.time()
                nodePath = path[1]
                weightPath = path[0]
                
            counter += 1
            timeTaken =  end_time - start_time
            totalTimeTaken += timeTaken
            
            totalNodePathLengths += len(nodePath)
            totalWeightPathLengths += weightPath

    averageTimeTaken = totalTimeTaken / counter
    averageSolutionLengthInNode = totalNodePathLengths / counter
    averageSolutionLengthInWeight = totalWeightPathLengths/ counter
    
    return (averageTimeTaken, averageSolutionLengthInNode, averageSolutionLengthInWeight)


totalDfsResult = []
totalBfsResult = []
totalDijkstraResult = []
totalAstarResult = []

# To find the average time and pathlength using dfs

result = evaluate('dfs','1xGraph.txt', '1xCityLocations.txt')
totalDfsResult.append(result)

result = evaluate('dfs', '2x.txt', '2xLocations.txt')
totalDfsResult.append(result)

result = evaluate('dfs', '3x.txt', '3xLocations.txt')
totalDfsResult.append(result)

result = evaluate('dfs', '4x.txt', '4xLocations.txt')
totalDfsResult.append(result)

#To find the average time and pathlength using bfs

result = evaluate('bfs',  '1xGraph.txt', '1xCityLocations.txt')
totalBfsResult.append(result)

result = evaluate('bfs', '2x.txt', '2xLocations.txt')
totalBfsResult.append(result)

result = evaluate('bfs', '3x.txt', '3xLocations.txt')
totalBfsResult.append(result)

result = evaluate('bfs', '4x.txt', '4xLocations.txt')
totalBfsResult.append(result)


# To find the average time and pathlength using dijkstra

result = evaluate('dijkstra', '1xGraph.txt', '1xCityLocations.txt')
totalDijkstraResult.append(result)

result = evaluate('dijkstra', '2x.txt', '2xLocations.txt')
totalDijkstraResult.append(result)

result = evaluate('dijkstra', '3x.txt', '3xLocations.txt')
totalDijkstraResult.append(result)

result = evaluate('dijkstra', '4x.txt', '4xLocations.txt')
totalDijkstraResult.append(result)

# To find the average time and pathlength using astar

result = evaluate('astar', '1xGraph.txt', '1xCityLocations.txt')
totalAstarResult.append(result)

result = evaluate('astar', '2x.txt', '2xLocations.txt')
totalAstarResult.append(result)

result = evaluate('astar', '3x.txt', '3xLocations.txt')
totalAstarResult.append(result)

result = evaluate('astar', '4x.txt', '4xLocations.txt')
totalAstarResult.append(result)


# print(totalDfsResult)
# print(totalBfsResult)
# print(totalDijkstraResult)
# print(totalAstarResult)

bfsTime = []
bfsLength = []
dfsTime = []
dfsLength = []
dijkstraTime = []
dijkstraNodeLength = []
dijkstraWeightLength = []
astarTime = []
astarNodeLength = []
astarWeightLength = []

for i in totalBfsResult:
    bfsTime.append(i[0])
    bfsLength.append(i[1])

for i in totalDfsResult:
    dfsTime.append(i[0])
    dfsLength.append(i[1])

for i in totalDijkstraResult:
    dijkstraTime.append(i[0])
    dijkstraNodeLength.append(i[1])
    dijkstraWeightLength.append(i[2])

for i in totalAstarResult:
    astarTime.append(i[0])
    astarNodeLength.append(i[1])
    astarWeightLength.append(i[2])



# for iv, (k, v) in enumerate(m.verticies.items()):
#     print(v.name)

# for iv, (k, edge) in enumerate(m.edges.items()):
#     print(edge.right.name, edge.left.name, edge.weight)
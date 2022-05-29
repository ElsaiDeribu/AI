from evaluate import *
import numpy as np
from matplotlib import pyplot as plt

# graph for time comaprisiond
graphSize = ['1x', '2x', ' 3x', '4x']
w = 0.2
bar1 = np.arange(len(graphSize))
bar2 = [i+w for i in bar1]
bar3 = [i+w for i in bar2]
bar4 = [i+w for i in bar3]


plt.bar(bar1, bfsTime,width = w, label = "BFS", color = "red")
plt.bar(bar2, dfsTime,width = w, label = "DFS", color = "blue")
plt.bar(bar3, dijkstraTime,width = w, label = "Dijkstra", color = "yellow")
plt.bar(bar4, astarTime,width = w, label = "Astar",color = "green")
plt.xlabel("Graph size relative to the original size")
plt.xticks([i + 0.1 for i in bar2], graphSize )
plt.ylabel("Average time taken to find the destination")
plt.legend()
plt.title("Time benchmark for all the algoritms")
plt.show()


# graph for solution length interms of path Nodes comparision 
graphSize = ['1x', '2x', ' 3x', '4x']
w = 0.2
bar1 = np.arange(len(graphSize))
bar2 = [i+w for i in bar1 ]
bar3 = [i+w for i in bar2]
bar4 = [i+w for i in bar3]


plt.bar(bar1, bfsLength,width = w, label = "BFS", color = "red")
plt.bar(bar2, dfsLength,width = w, label = "DFS", color = "blue")
plt.bar(bar3, dijkstraNodeLength,width = w, label = "Dijkstra", color = "yellow")
plt.bar(bar4, astarNodeLength,width = w, label = "Astar",color = "green")
plt.xlabel("Graph size relative to the original size")
plt.xticks([i + 0.1 for i in bar2], graphSize )
plt.ylabel("Average solution length interms of path Nodes")
plt.legend()
plt.title("Solution length benchmark for all algothms interms of path Nodes")
plt.show()

#graph for dfs vs bfs solution length comparision

graphSize = ['1x', '2x', ' 3x', '4x']

w = 0.2
bar1 = np.arange(len(graphSize))
bar2 = [i+w for i in bar1 ]

plt.bar(bar1, bfsLength,width = w, label = "BFS", color = "red")
plt.bar(bar2, dfsLength,width = w, label = "DFS", color = "blue")

plt.xlabel("Graph size relative to the original size")
plt.xticks([i + 0.1 for i in bar1], graphSize )
plt.ylabel("Average solution length interms of path Nodes")
plt.legend()
plt.title("Solution length benchmark for DFS and BFS")
plt.show()


# graph for dijkstra vs astar solution length comparision
graphSize = ['1x', '2x', ' 3x', '4x']
w = 0.2
bar1 = np.arange(len(graphSize))
bar2 = [i + w for i in bar1 ]

plt.bar(bar1, dijkstraWeightLength,width = w, label = "Dijkstra", color = "yellow")
plt.bar(bar2, astarWeightLength,width = w, label = "Astar", color = "green")

plt.xlabel("Graph size relative to the original size")
plt.xticks([i + 0.1 for i in bar1], graphSize )
plt.ylabel("Average solution length interms of path weight")
plt.legend()
plt.title("Solution length benchmark Dijkstra and Astar")
plt.show()


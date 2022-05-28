from collections import deque
import heapq
from numpy import power
from math import cos, asin, sqrt, pi

class Node:
    def __init__(self, name):
        self.name = name
        self.edge_list = []

    def connect(self, node):
        con = (self.name, node.name)
        self.edge_list.append(con)

class Edge:
    def __init__(self, left, right, weight=1):
        self.left = left
        self.right = right
        self.weight = weight

class Graph:

    def __init__(self):
        self.verticies = {}
        self.edges = {}


    def add_node(self, node):
        self.verticies[node.name] = node
    
    def add_edge(self, left, right, weight = 1):
        if left.name not in self.verticies:
            self.verticies[left.name] = left
        
        if right.name not in self.verticies:
            self.verticies[right.name] = right

        e = Edge(left, right, weight)


        key = (left.name, right.name)
        self.edges[key] = e

        key = (right.name, left.name)
        self.edges[key] = e

        self.verticies[left.name].connect(right)
        self.verticies[right.name].connect(left)
        
        
    def dfs(self, startNode, requiredNode):
        
        path = []
        
        def helper(givenNode, requiredNode, path):
            path.append(givenNode.name)
            if givenNode.name == requiredNode.name:
                return path[:]
            
            for neighbor in givenNode.edge_list:
                if neighbor[1] not in path:
                    temp =  helper(self.verticies[neighbor[1]], requiredNode, path[:])
                    if temp:
                        return temp
        
            path.pop()
                    
        return helper(startNode, requiredNode, path)
    
    
    def bfs(self, startNode, requiredNode):
        visited = set()
        queue = deque()
        queue.append((startNode.name, []))
        visited.add(startNode.name)
        
        while queue:
            v, path = queue.popleft()
            path.append(v)
            if v == requiredNode.name:
                return path
            for _, neighbour in self.verticies[v].edge_list:
                if neighbour not in visited:
                    queue.append((neighbour, path[:]))
                    visited.add(neighbour)
    
        return 0
    
    def dijkstra(self, startNode, requiredNode):
        
        heap = []
        distances = {k: power(10,5) for k in self.verticies.keys()}
        predecessors = {}
        distances[startNode.name] = 0 
        heapq.heappush(heap, (0, startNode.name))

        while heap:
            last_w, curr_v = heapq.heappop(heap)
            if curr_v == requiredNode.name:
                break
            for connnection in self.verticies[curr_v].edge_list:
                neighbour = connnection[1]
                neighbour_w = self.edges[(curr_v, neighbour)].weight
                cand_w = last_w + neighbour_w 
        
                if cand_w < distances[neighbour]:
                    distances[neighbour] = cand_w
                    predecessors[neighbour] = curr_v
                    heapq.heappush(heap, (cand_w, neighbour))

        path = []
        path.append(requiredNode.name)
        
        def recur(destination):
            path.append(predecessors[destination])
            if predecessors[destination] == startNode.name:
                return
            recur(predecessors[destination])
            
        if predecessors:
            recur(requiredNode.name)
        
        return (distances[requiredNode.name], path[::-1])


            
    def astar(self, startNode, requiredNode):
        
        readLocations = {}
        
        file = open('cityLocations.txt', 'r')
        f = file.readlines()

        for line in f:
            line = (line.strip()).split(' ')
            readLocations[line[0]] = (float(line[1]), float(line[2]))
        
        
        def findHeuristic(node):
            
            lat1, lon1 = readLocations[requiredNode.name]
            lat2, lon2 = readLocations[node]
            
            return distance(lat1, lon1, lat2, lon2)
        
        def distance(lat1, lon1, lat2, lon2):
            p = pi/180
            a = 0.5 - cos((lat2-lat1)*p)/2 + cos(lat1*p) * cos(lat2*p) * (1-cos((lon2-lon1)*p))/2
            return 12742 * asin(sqrt(a)) 


        
        heap = []
        distances = {node: power(10,5) for node in self.verticies.keys()}
        predecessors = {}
        distances[startNode.name] = 0 
        heapq.heappush(heap, (0 + findHeuristic(startNode.name), startNode.name))

        while heap:
            last_w, curr_v = heapq.heappop(heap)
            if curr_v == requiredNode.name:
                break
            for connnection in self.verticies[curr_v].edge_list:
            
                neighbour = connnection[1]
                neighbour_w = self.edges[(curr_v, neighbour)].weight 
                cand_w = last_w - findHeuristic(curr_v) + neighbour_w 
                
                # f = cand_w + findHeuristic(neighbour)
                
                if cand_w < distances[neighbour]:
                    distances[neighbour] = cand_w 
                    predecessors[neighbour] = curr_v
                    heapq.heappush(heap, (cand_w  + findHeuristic(neighbour), neighbour))

        path = []
        path.append(requiredNode.name)

        def recur(destination):
            path.append(predecessors[destination])
            if predecessors[destination] == startNode.name:
                return
            recur(predecessors[destination])
        if predecessors:
            recur(requiredNode.name)
        
        return (distances[requiredNode.name], path[::-1])
            



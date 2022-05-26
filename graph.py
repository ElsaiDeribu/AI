from collections import deque

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
        
        # print(self.verticies[left.name].edge_list)
        # print(left.edge_list)
        
        
        
    def dfs(self, startNode, requiredNode):
        
        self.shortest = [1] * power(10,5)
        path = []
        
        def helper(givenNode, requiredNode, path):
            path.append(givenNode.name)
            if givenNode.name == requiredNode.name:
                if len(path) < len(self.shortest):
                    self.shortest = path[:]
            
            for neighbor in givenNode.edge_list:
                if neighbor[1] not in path:
                    helper(self.verticies[neighbor[1]], requiredNode, path[:])
        
            path.pop()
                    
        helper(startNode, requiredNode, path)
        
        return self.shortest
    
        
    # def dfs (self, startNode, requiredNode):
        
    #     if startNode.name == requiredNode.name:
    #         return startNode
    #     path = [] 
    #     visited = set()
    #     st = []
    #     st.append(startNode.name)
    #     path.append(startNode.name)
    #     while st:
    #         v = st.pop()
    #         if v not in visited:
    #             visited.add(v)
    #             path.append(v)
    #         for _, neighbourName in self.verticies[v].edge_list:
    #             if neighbourName == requiredNode.name:
    #                 return self.verticies[neighbourName]
    #             if neighbourName not in visited:
    #                 st.append(neighbourName)
    #     return 0
    
    
    
    
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
    
            
        print(visited)
            
        return 0
    
    def djikstra(startNode, destination):
        shortest_distance = {}
        
        
        
    def search(self, a, b):
        pass

    def to_aj_matrix(self):
        pass








a = Node('A')
b = Node('B')
c = Node('C') 
d = Node('D')
e = Node('E')
k = Node('K')
l = Node('L')

g = Graph()
g.add_edge(a, e)
g.add_edge(a, c)
g.add_edge(a, d)
g.add_edge(b, c)
g.add_edge(b, e)
g.add_edge(b, l)
g.add_edge(l, k)
g.add_edge(k, e)

# print(g)
# for iv, (k, v) in enumerate(g.verticies.items()):
#     print(v.name)

# for iv, (k, edge) in enumerate(g.edges.items()):
#     print(edge.right.name, edge.left.name, edge.weight)




# ans = g.bfs(d,l)

# print(ans)



m = Graph()

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
        m.add_edge(a, b, int(edge[2]))
        
    else:
        node = temp
        a = Node(node[0])
        m.add_node(a)
    



a = m.verticies["Neamt"]
b = m.verticies["Craiova"]


ans = m.bfs(a, b)
print(ans)

# ans = m.dfs(a, b)
# print(ans)











# for iv, (k, v) in enumerate(m.verticies.items()):
#     print(v.name)

# for iv, (k, edge) in enumerate(m.edges.items()):
#     print(edge.right.name, edge.left.name, edge.weight)
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
    
    def add_edge(self, left, right, weight=1):
        if left.name not in self.verticies:
            self.verticies[left.name] = left
        
        if right.name not in self.verticies:
            self.verticies[right.name] = right

        e = Edge(left, right, weight=1)


        key = (left.name, right.name)
        self.edges[key] = e

        key = (right.name, left.name)
        self.edges[key] = e

        left.connect(right)
        right.connect(left)
        
    def dfs (self, startNode, requiredNode):
        visited = set()
        st = []
        st.append(startNode.name)
        while st:
            v = st.pop()
            if v not in visited:
                visited.add(v)
            for neighbourName in self.verticies[v].edge_list[1]:
                if neighbourName == requiredNode.name:
                    return self.verticies[neighbourName]
                if self.verticies[neighbourName] not in visited:
                    st.append(self.verticies[neighbourName])
        return 0
    
    def bfs(self, startNode, requiredNode):
        visited = set()
        queue = []
        queue.append(startNode.name)
        visited.add(startNode.name)
        while queue:
            v = queue.pop(0)
            for neighbour in self.verticies[v].edge_list[1]:
                if neighbour == requiredNode.name:
                    return self.verticies[neighbour]
                if neighbour not in visited:
                    queue.append(neighbour)
                    visited.add(neighbour)
            
        return 0
        

    def search(self, a, b):
        pass

    def to_aj_matrix(self):
        pass


a = Node('A')
b = Node('B')
c = Node('C')
d = Node('D')
e = Node('E')

g = Graph()
g.add_edge(a, e)
g.add_edge(a, c)
g.add_edge(a, d)
g.add_edge(b, c)
g.add_edge(b, e)

# print(g)
for iv, (k, v) in enumerate(g.verticies.items()):
    print(v.name)

for iv, (k, edge) in enumerate(g.edges.items()):
    print(edge.right.name, edge.left.name, edge.weight)



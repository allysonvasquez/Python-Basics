"""
Graph ADT Is Defined:
Graph()
addVertex(vert)                 - adds an instance of Vertex to the Graph
addEdge(fromVert, toVert)       - adds a new, directed edge to connect two vertices
addEdge(fromVert,tovert, weight)- adds a new, weighted, dirrected edge to connect two vertices
getVertex(vertKey)              - finds the vertex in the graph named vertKey
getVertices()                   - returns Trrue if (vertex in graph). False otherwise

Two main ways to implement Graphs in Python: Adjacency Matrix & Adjacency List
ADJACENCY MATRIX-----
- Each row nad column represent a vertex in the graph
- Value stored in the cell at the intersection of row(v) and col(w) indicate if there is an edge
- Vertices are adjacent if they are connected by an edge
PROS:   Simple and good for small graphs to see which nodes are connected to other nodes
CONS:   Many cells in the matrix can be empty (Sparse)
        The number of edges required to fill a matrix is V^2

ADJACENCY LIST-----
- Keeps a master list of all vertices in the Graph object
- Each vertex object maintains a list of connected vertices
- Uses a Dictionary: Keys are the vertices, values are the weights
PROS:   More space-efficient to timplement sparsely connected graphs
        Can easily find all the links that are directly connected to a particular vertex
"""
#Vertex represents each vertex within the graph
class Vertex:
    def __init__(self, key):
        self.id = key  # Usually a string
        self.connectedTo = {}   # Keeps trrack of connected vertices & weight of each edge
    
    def __str__(self):
        return str(self.id) + " connectedTo: " + str([x.id for x in self.connectedTo])

    def addNeighbor(self, neighbor, weight=0):
        self.connectedTo[neighbor] = weight
    
    def getConnections(self):
        return self.connectedTo.keys()
    
    def getWeight(self, neighbor):
        return self.connectedTo[neighbor]
    
    def getId(self):
        return self.id
    
# Graph Holds the master list of vertices
class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0
    
    def addVertex(self, key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex
    
    def getVertex(self, n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None
    
    def __contains__(self,n):
        return n in self.vertList
    
    def addEdge(self, fromVert, toVert, weight=0):
        if fromVert not in self.vertList:
            nv = self.addVertex(fromVert)
        if toVert not in self.vertList:
            nv = self.addVertex(toVert)
        self.vertList[fromVert].addNeighbor(self.vertList[toVert], weight)
    
    def getVertices(self):
        return self.vertList.keys()
    
    def __iter__(self):  # iterate over all vertex objects in graph
        return iter(self.vertList.values())

# creating a graph
g = Graph()

for i in range(6):
    g.addVertex(i)

g.addEdge(0,1,5)
g.addEdge(0,5,2)
g.addEdge(1,2,4)
g.addEdge(2,3,9)
g.addEdge(3,4,7)
g.addEdge(3,5,3)
g.addEdge(4,0,1)
g.addEdge(5,4,8)
g.addEdge(5,2,1)

for v in g:
    for w in v.getConnections():
        print("( %s , %s )" % (v.getId(), w.getId()))
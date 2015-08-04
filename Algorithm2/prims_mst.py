import sys
from operator import itemgetter

class Vertex(object):
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}

    def addNeighbor(self, nbr, weight = 0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self, nbr):
        return self.connectedTo[nbr]

class Graph(object):
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

    def __contains__(self, n):
        return n in self.vertList

    def addEdge(self, f, t, cost = 0):
        if f not in self.vertList:
            self.addVertex(f)
        if t not in self.vertList:
            self.addVertex(t)
            
        self.vertList[f].addNeighbor(self.vertList[t], cost)
        self.vertList[t].addNeighbor(self.vertList[f], cost)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())

def loaddata(filename):
    f = open(filename)
    content = f.read()
    lines = content.splitlines()

    num_nodes = int(lines[0].split()[0])
    num_edges = int(lines[0].split()[1])

    g = Graph()
    for i in range(num_nodes):
        g.addVertex(i)

    for line in lines[1:]:
        node1 = int(line.split()[0])
        node2 = int(line.split()[1])
        cost = int(line.split()[2])
        g.addEdge(node1 - 1, node2 - 1, cost)

    return num_nodes, num_edges, g

def prim(graph, num_nodes):
    T = list()
    X = set()

    X.add(0)

    while len(X) != num_nodes:
        print('Current len of X is: %d' % len(X))
        crossing = set()
        for x in X:
            for k in range(num_nodes):
                if k not in X:
                    v = graph.getVertex(x)
                    w = graph.getVertex(k)
                    if w in v.getConnections():
                        crossing.add((x, k, v.getWeight(w)))
        edge = sorted(crossing, key = itemgetter(2))[0]
        T.append(edge[2])
        X.add(edge[1])

    return T

def sum_list(lst):
    total = 0
    for i in lst:
        total += i
    return total

filename = 'edges.txt'
n_nodes, n_edges, graph = loaddata(filename)
result = prim(graph, n_nodes)
# for v in graph:
#     for w in v.getConnections():
#         print('(%s, %s, %s)' % (v.getId(), w.getId(), v.getWeight(w)))

print('minimum spanning tree is: %s, sum is: %s' % (result, sum_list(result)))
        

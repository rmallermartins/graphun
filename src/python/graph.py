from sys import maxint

def makeGraph(filename):
    f = open(filename)
    data = f.readlines()
    data = [(a.strip()) for a in data]
    div = data.index("#")
    vertexes = data[:div]
    edges = data[div+1:]
    edges = [(e.split(' ')) for e in edges]
    adjList = makeAdjList(vertexes, edges)
    return vertexes, edges, adjList

def makeAdjList(vertexes, edges):
    adjList = {}
    for v in vertexes:
        adjList[v] = []
    for e in edges:
        adjList[e[0]].append(e[1])
    return adjList
    
def makeAdjMatrix(vertexes, edges, adjList):
    adjMatrix = [[0 for x in xrange(len(vertexes))] for x in xrange(len(vertexes))]
    weight = makeWeightList(edges)
    for u in vertexes
        for v in adjList[u]
            adjMatrix[u][v] = weight[(u, v)]
    return adjMatrix
            
    
def makeWeightList(edges):
    weightList = {}
    for e in edges:
        weightList[(e[0], e[1])] = int(e[2])
    return weightList
    
def transpose(edges):
    edgesT = {}
    eT = {}
    for e in edges:
        eT[0] = e[1]
        eT[1] = e[0] 
    return edgesT

def relax(u, v, w, pi, dist):
    if dist[v] > dist[u] + w:
        dist[v] = dist[u] + w
        pi[v] = u
    return pi, dist

def initializeSingleSource(V, E, s, pi, dist):
    for v in V:
        dist[v] = maxint
        pi[v] = None
    dist[s] = 0
    pi[s] = None
    return pi, dist

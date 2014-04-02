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
    
def transpose(edges):
    for e in edges:
        edgesT[0] = e[1]
        edgesT[1] = e[0]
    return edgesT

def readFile(filename):
    vertexes = list()
    edges = list()
    isEdge = False
    f = open(filename)
    for line in f:
        if (line.strip("\n") == "#"):
            isEdge = True
        else:
            if not isEdge:
                vertexes.append(line.strip("\n"))
            else:
                edge = line.strip("\n").split(" ") 
                edges.append(edge)
    f.close()
    return vertexes, edges

def makeGraph(vertexes, edges):
    graph = dict()
    adjList = list()
    for vertex in vertexes:
        graph[vertex] = makeAdjList(vertex, edges)

def makeAdjList(vertex, edges):
    adjList = list()
    for edge in edges:
        if edge[0] = vertex
            adjList.append(edge[1])
    return adjList

import graph

def execute(V, E, adjList):
    dfs(V, E, adjList)
    ET = graph.transpose(E)
    transpAdjList = graph.makeAdjList(V, ET)

def dfs(V, E, adjList):
    global color
    global dist
    global final
    global pi
    global time
    for u in V:
        color[u] = 'white'
    time = 0
    for u in V:
        if color[u] == 'white':
            dfs-visit(u, adjList)
            
def dfs-visit(u, adjList):
    time += 1
    color[u] = 'grey'
    dist[u] = time
    for v in adjList[u]:
        if color[v] == 'white'
            dad[v] = u
            dfs-visit(v)
    color[u] = 'preto'
    time += 1
    final[u] = time

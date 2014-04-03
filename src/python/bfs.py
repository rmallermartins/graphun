from collections import deque 

def execute(V, E, s, adjList):
    global dist
    global color
    dist = {}
    color = {}
    for u in V:
        dist[u] = 0
        color[u] = 'white'
    color[s] = 'grey'
    Q = deque()
    Q.append(s)
    while Q:
        u = Q.popleft()
        for v in adjList[u]:
            if color[v] == 'white':
                dist[v] = dist[u] + 1
                color[v] = 'grey'
                Q.append(v)
        color[u] = 'black'
    printBfs(V, E, s)
    return dist
    
def printBfs(V, E, s):
    for u in V:
        if s == u:
            print s + ' ' + u + ' ' + str(dist[u])
        elif dist[u] != 0:
            print s + ' ' + u + ' ' + str(dist[u])

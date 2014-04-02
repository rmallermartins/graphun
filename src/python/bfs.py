from collections import deque 

def execute(V, E, s, adjList):
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
    return dist
    
def printOut(V, E, s, distList):
    for u in V:
        if s == u:
            print s + ' ' + u + ' ' + str(distList[u])
        elif distList[u] != 0:
            print s + ' ' + u + ' ' + str(distList[u])

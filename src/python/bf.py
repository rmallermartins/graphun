from sys import maxint

def execute(V, E, s):
    global dist
    global pi
    dist = {}
    pi = {}
    initializeSingleSource(V, E, s)
    for i in range(1, len(V)-1):
        for e in E:
            relax(e[0], e[1], int(e[2]))
    for e in E:
        if dist[e[1]] > dist[e[0]] + int(e[2]):
            print "Erro, grafo contem ciclo negativo"
    printBf(V, s)
    

def relax(u, v, w):
    if dist[v] > dist[u] + w:
        dist[v] = dist[u] + w
        pi[v] = u

def initializeSingleSource(V, E, s):
    for v in V:
        dist[v] = maxint
    dist[s] = 0
    pi[s] = None
    
def printBf(V, s):
    for v in V:
        printPath(s, v)
        if dist[v] < maxint:
            print dist[v]

def printPath(s, v):
    if s == v:
        print s,
    elif pi[v] == None:
        None
    else:
        printPath(s, pi[v])
        print v,
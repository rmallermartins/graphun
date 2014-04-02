from sys import maxint

def execute(V, E, s):
    global dist = {}
    global pi = {}
    initialize-single-source(V, E, s)
    for i in range(1, len(V)-1):
        for e in E:
            relax(e[0], e[1], e[2])
    for e in E:
        if dist[e[1]] > dist[e[0]] + e[2]
            return False
    return True

def relax(u, v, w):
    if dist[v] > dist[u] + w
        dist[v] = dist[u] + w
        pi[v] = u

def initialize-single-source(V, E, s):
    for v in V:
        dist[v] = maxint
    dist[s] = 0
    
def printOut(V, dist):
    

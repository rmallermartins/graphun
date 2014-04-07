from sys import maxint
import graph

def execute(V, E, s, weight):
    global dist
    global pi
    dist = {}
    pi = {}
    pi, dist = graph.initializeSingleSource(V, E, s, pi, dist)
    for i in range(1, len(V)-1):
        for e in E:
            pi, dist = graph.relax(e[0], e[1], weight[(e[0], e[1])], pi, dist)
    for e in E:
        if dist[e[1]] > dist[e[0]] + weight[(e[0], e[1])]:
            print "Erro, grafo contem ciclo negativo"
    printBf(V, s)
    
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

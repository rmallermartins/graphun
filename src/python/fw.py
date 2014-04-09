from sys import maxint

def execute(nVertex, W):
    global Pi
    n = len(W)
    D = W
    Pi = [[None for x in xrange(len(nVertex))] for x in xrange(len(nVertex))]
    
    for i in range(1, n):
        for j in range(1, n):
            if i != j and W[i][j] < maxint:
                Pi[i][j] = i
                
    for k in range(1, n):
        for i in range(1, n):
            for j in range(1, n):
                if D[i][j] > D[i][k] + D[k][j]:
                    D[i][j] = D[i][k] + D[k][j]
                    Pi[i][j] = Pi[k][j]
    
    printFw(nVertex, D)
    
def printFw(nVertex, D):
    for u in D:
        for v in D[nVertex[u]]:
            printPath(nVertex[u], nVertex[v])
            if D[nVertex[u]][nVertex[v]] < maxint:
                print D[nvertex[u]][nVertex[v]]
            
def printPath(s, v):
    if s == v:
        print s,
    elif Pi[s][v] == None:
        None
    else:
        printPath(s, Pi[s][v])
        print v,

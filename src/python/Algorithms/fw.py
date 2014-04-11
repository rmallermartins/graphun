import sys
sys.path.append("../Structures/")
from sys import maxint

class Fw:

    def execute(self, G, W):
        n = G.getNVertex()
        D = W
        Pi = [[None for x in range(n)] for x in range(n)]
        for i in range(0, n):
            for j in range(0, n):
                if i != j and W[i][j] < maxint:
                    Pi[i][j] = i
        for k in range(0, n):
            for i in range(0, n):
                for j in range(0, n):
                    if D[i][j] > D[i][k] + D[k][j]:
                        D[i][j] = D[i][k] + D[k][j]
                        Pi[i][j] = Pi[k][j]
    
        self.printFw(G, D, Pi)
    
    def printFw(self, G, D, Pi):
        for u in D:
            for v in D[v]:
                printPath(u.getId(), v.getId(), Pi)
                if D[u.getId()][v.getId()] < maxint:
                    print D[u.getId()][v.getId()]
            
    def printPath(self, s, v, Pi):
        if s == v:
            vertex = G.getVertexes()[s]
            print vertex.getName(),
        elif Pi[s][v] == None:
            None
        else:
            printPath(s, Pi[s][v], Pi)
            vertex = G.getVertexes()[v]
            print vertex.getName(),

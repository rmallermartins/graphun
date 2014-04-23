import sys
sys.path.append("../Structures/")
from sys import maxint

class Fw:

    def execute(self, G, W):
        n = G.getNVertex()
        D = W
        Pi = [[None for x in range(n)] for x in range(n)]
        for key, i in G.getVertexes().iteritems():
            for key, j in G.getVertexes().iteritems():
                if i != j and W[i.getId()][j.getId()] < maxint:
                    Pi[i.getId()][j.getId()] = i
        for k in range(0, n):
            for i in range(0, n):
                for j in range(0, n):
                    if D[i][j] > D[i][k] + D[k][j] and D[i][k] != maxint and D[k][j] != maxint:
                        D[i][j] = D[i][k] + D[k][j]
                        Pi[i][j] = Pi[k][j]
                    if i == j:
                        D[i][j] = 0
        self.printFw(G, D, Pi, n)
    
    def printFw(self, G, D, Pi, n):
        for key, u in G.getVertexes().iteritems():
            for key, v in G.getVertexes().iteritems():
                self.printPath(u, v, Pi)
                if D[u.getId()][v.getId()] < maxint:
                    print D[u.getId()][v.getId()]
            
    def printPath(self, s, v, Pi):
        if s == v:
            print v.getName(),
        elif Pi[s.getId()][v.getId()] == None:
            None
        else:
            self.printPath(s, Pi[s.getId()][v.getId()], Pi)
            print v.getName(),

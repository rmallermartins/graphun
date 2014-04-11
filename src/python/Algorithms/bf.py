import sys
sys.path.append("../Structures/")
from sys import maxint
import graph

class Bf:

    def execute(self, G, s):
        G.initializeSingleSource(s)
        for i in range(1, len(G.getVertexes()) - 1):
            for key, e in G.getEdges().iteritems():
                self.relax(e.getOrig(), e.getDest(), e.getW())  
        for key, e in G.getEdges().iteritems():
            if e.getDest().getD() > e.getOrig().getD() + e.getW():
                print "Erro, grafo contem ciclo negativo"
        self.printBf(G, s)
    
    def relax(self, u, v, w):
        if v.getD() > u.getD() + w:
            v.setD(u.getD() + w)
            v.setPi(u)
    
    def printBf(self, G, s):
        for key, v in G.getVertexes().iteritems():
            self.printPath(s, v)
            if v.getD() < maxint:
                print v.getD()

    def printPath(self, s, v):
        if s.getName() == v.getName():
            print s.getName(),
        elif v.getPi() == None:
            None
        else:
            self.printPath(s, v.getPi())
            print v.getName(),

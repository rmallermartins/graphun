from sys import maxint
import graph

class Bf:

    def execute(self, G, s):
        G.initializeSingleSource(s)
        for i in range(1, len(G.V) - 1):
            for i in range(len(G.E)):
                e = G.E[i]
                G.relax(e.orig, e.dest, e.w)  
        for i in range(len(G.E)):
            e = G.E[i]
            if e.dest.d > e.orig.d + e.w:
                print "Erro, grafo contem ciclo negativo"
        self.printBf(G, s)
    
    def printBf(self, G, s):
        for key, v in G.V.iteritems():
            self.printPath(s, v)
            if v.d < maxint:
                print v.d

    def printPath(self, s, v):
        if s.name == v.name:
            print s.name,
        elif v.pi == None:
            None
        else:
            self.printPath(s, v.pi)
            print v.name,

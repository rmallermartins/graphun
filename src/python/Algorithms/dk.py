import sys
sys.path.append("../Structures/")
from sys import maxint
import graph
import heapq

class Dk:

    def execute(self, G, s):
        G.initializeSingleSource(s)
        S = []
        Q = []
        for key, v in G.getVertexes().iteritems():
            heapq.heappush(Q, (v.getD(), v.getId(), v))
        
        while Q:
            (d, index, u) = heapq.heappop(Q)
            for key in u.getAdjList():
                v = G.getVertexes()[key]
                e = G.getEdges()[u.getName() + ' ' + v.getName()]
                self.relax(Q, u, v, e.getW())
        self.printDk(G, s)
           
    def relax(self, Q, u, v, w):
        if v.getD() > u.getD() + w:
            v.setD(u.getD() + w)
            v.setPi(u)
            heapq.heappush(Q, (v.getD(), v.getId(), v))
    
    def printDk(self, G, s):
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

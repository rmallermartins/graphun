import sys
sys.path.append("../Structures/")
from collections import deque

class Dfs:
    __time = 0

    def executeNormal(self, G):
        for key, u in G.getVertexes().iteritems():
            u.setColor('white')
            u.setPi(None)
        vertexSeq = []
        self.__time = 0
        for key, u in G.getVertexes().iteritems():
            if u.getColor() == 'white':
                self.dfsVisit(G, u, vertexSeq)
        return vertexSeq
                
    def executeTransp(self, G, vertexSeq):
        sccList = []
        for key, u in G.getVertexes().iteritems():
            u.setColor('white')
            u.setPi(None)
        vertexSeq.sort
        vertexSeq.reverse
        self.__time = 0
        for u in vertexSeq:
            if u.getColor() == 'white':
                self.dfsVisit(G, u, sccList)
        return sccList
            
    def dfsVisit(self, G, u, vertexSeq):
        self.__time += 1
        u.setColor('grey')
        u.setD(self.__time)
        for key in u.getAdjList():
            v = G.getVertexes()[key]
            if v.getColor() == 'white':
                v.setPi(u)
                self.dfsVisit(G, v, vertexSeq)         
        u.setColor('black')
        self.__time += 1
        u.setF(self.__time)
        vertexSeq.append(u)

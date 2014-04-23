import sys
sys.path.append("../Structures/")
from collections import deque

class Dfs:
    __time = 0
    __sccList = []
    __vertexSeq = []

    def executeNormal(self, G):
        for key, u in G.getVertexes().iteritems():
            u.setColor('white')
            u.setPi(None)
        self.__time = 0
        for key, u in G.getVertexes().iteritems():
            if u.getColor() == 'white':
                self.dfsVisit(G, u, self.__vertexSeq)
                
    def executeTransp(self, G):
        for key, u in G.getVertexes().iteritems():
            u.setColor('white')
            u.setPi(None)
        self.__time = 0
        self.__vertexSeq.reverse()
        for u in self.__vertexSeq:
            if u.getColor() == 'white':
                self.dfsVisit(G, u, self.__sccList)
            
    def dfsVisit(self, G, u, seqList):
        self.__time += 1
        u.setColor('grey')
        u.setD(self.__time)
        for key in u.getAdjList():
            v = G.getVertexes()[key]
            if v.getColor() == 'white':
                v.setPi(u)
                self.dfsVisit(G, v, seqList)         
        u.setColor('black')
        self.__time += 1
        u.setF(self.__time)
        seqList.append(u)
    
    def getSccList(self):
        return self.__sccList

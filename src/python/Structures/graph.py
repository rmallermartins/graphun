from sys import maxint
from vertex import Vertex
from edge import Edge

class Graph(object):

    def __init__(self):
        self.__V = {}
        self.__E = []
        self.__nVertex = 0
    
    def buildGraph(self, filename):
        f = open(filename)
        isVertex = True
        index = 0
        for line in f:
            line = line.strip()
            if isVertex == True and line != "#":
                self.addVertex(line)
            elif line == "#":
                isVertex = False                
            elif isVertex == False:
                edge = line.split(' ')
                if len(edge) == 2:
                    self.addEdge(self.__V[edge[0]], self.__V[edge[1]], 0)
                else:
                    self.addEdge(self.__V[edge[0]], self.__V[edge[1]], int(edge[2]))
        self.makeAdjLists()
                    

    def makeAdjLists(self):
        for e in self.__E:
            self.__V[e.getOrig().getName()].addAdjVertex(e.getDest().getName())
    
    def relax(self, u, v, w):
        if v.getD() > u.getD() + w:
            v.setD(u.getD() + w)
            v.setPi(u)

    def initializeSingleSource(self, s):
        for key, v in self.__V.iteritems():
            v.setD(maxint)
            v.setPi(None)
        s.setD(0)
        s.setPi(None)
             
    def getVertexes(self):
        return self.__V
    
    def addVertex(self, name):
        newVertex = Vertex(self.__nVertex, name)
        self.__V[name] = newVertex
        self.__nVertex += 1
    
    def addEdge(self, orig, dest, w):
        newEdge = Edge(orig, dest, w)
        self.__E.append(newEdge)
    
    def getEdges(self):
        return self.__E
    
    def getNVertex(self):
        return self.__nVertex
    
    def getAdjMatrix(self):
        matrix = [[maxint for i in range(self.__nVertex)] for j in range(self.__nVertex)]
        for e in self.__E:
            matrix[e.getOrig().getId()][e.getDest().getId()] = e.getW()
        return matrix

    def getInitVertex(self):
        for v in self.__V:
            if self.__V[v].getId() == 0:
                return self.__V[v]

    def getTransposed(edges): #TODO
        edgesT = {}
        eT = {}
        for e in edges:
            eT[0] = e[1]
            eT[1] = e[0] 
        return edgesT
    

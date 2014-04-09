from sys import maxint
from vertex import Vertex
from edge import Edge

class Graph(object):

    def __init__(self):
        self.V = {}
        self.E = []
    
    def readGraphFile(self, filename):
        f = open(filename)
        isVertex = True
        index = 0
        for line in f:
            line = line.strip()
            if isVertex == True and line != "#":
                v = Vertex(line, index)
                self.V[line] = v
                index += 1
            elif line == "#":
                isVertex = False                
            elif isVertex == False:
                edge = line.split(' ')
                if len(edge) == 2:
                    e = Edge(self.V[edge[0]], self.V[edge[1]], 0)
                    self.E.append(e)
                else:
                    e = Edge(self.V[edge[0]], self.V[edge[1]], int(edge[2]))
                    self.E.append(e)
                    

    def makeAdjLists(self):
        for e in self.E:
            self.V[e.orig].adjList.append(e.dest)
    
    def getInitVertex(self):
        for v in self.V:
            if self.V[v].index == 0:
                return self.V[v]
    
#    def makeAdjMatrix(self):  TODO

    def transpose(edges):
        edgesT = {}
        eT = {}
        for e in edges:
            eT[0] = e[1]
            eT[1] = e[0] 
        return edgesT
    
    def relax(self, u, v, w):
        if v.d > u.d + w:
            v.d = u.d + w
            v.pi = u

    def initializeSingleSource(self, s):
        for key, v in self.V.iteritems():
            v.d = maxint
            v.pi = None
        s.d = 0
        s.pi = None

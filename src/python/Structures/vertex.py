from sys import maxint

class Vertex(object):

    def __init__(self, index, name):
        self.__id = index
        self.__name = name
        self.__adjList = []
        self.__color = 'white'
        self.__pi = None
        self.__d = maxint
        self.__f = None
        
    def cleanAdjList(self):
        self.__adjList = []
        
    def getId(self):
        return self.__id
        
    def getName(self):
        return self.__name
    
    def getAdjList(self):
        return self.__adjList
    
    def addAdjVertex(self, vertex):
        self.__adjList.append(vertex)
    
    def getColor(self):
        return self.__color
        
    def setColor(self, value):
        self.__color = value
        
    def getPi(self):
        return self.__pi
    
    def setPi(self, vertex):
        self.__pi = vertex
        
    def getD(self):
        return self.__d
        
    def setD(self, value):
        self.__d = value
    
    def getF(self):
        return self.__f
        
    def setF(self, value):
        self.__f = value

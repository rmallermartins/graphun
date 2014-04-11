class Edge(object):

    def __init__(self, u, v, w):
        self.__orig = u
        self.__dest = v
        self.__w = w
        
    def getOrig(self):
        return self.__orig
    
    def getDest(self):
        return self.__dest
        
    def getW(self):
        return self.__w

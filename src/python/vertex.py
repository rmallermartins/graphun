from sys import maxint

class Vertex(object):

    def __init__(self, name, index):
        self.name = name
        self.index = index
        self.adjList = []
        self.color = 'white'
        self.pi = None
        self.d = maxint
        self.f = None

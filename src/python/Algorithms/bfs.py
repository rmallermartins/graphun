import sys
sys.path.append("../Structures/")
import graph
from collections import deque

class Bfs:
    
    def execute(self, G, s):
        for key, u in G.getVertexes().iteritems():
            u.setD(0)
        s.setColor('grey')
        Q = deque()
        Q.append(s)
        while Q:
            u = Q.popleft()
            for key in u.getAdjList():
                v = G.getVertexes()[key]
                if v.getColor() == 'white':
                    v.setD(u.getD() + 1)
                    v.setColor('grey')
                    Q.append(v)
            u.setColor('black')
        self.printBfs(G, s)
        
    def printBfs(self, G, s):
        for key, u in G.getVertexes().iteritems():
            if s.getName() == u.getName():
                print s.getName() + ' ' + u.getName() + ' ' + str(u.getD())
            elif u.getD() != 0:
                print s.getName() + ' ' + u.getName() + ' ' + str(u.getD())

import graph
from collections import deque

class Bfs:
    
    def execute(self, G, s):
        for key, u in G.V.iteritems():
            u.d = 0
        s.color = 'grey'
        Q = deque()
        Q.append(s)
        while Q:
            u = Q.popleft()
            for key in u.adjList:
                v = G.V[key]
                if v.color == 'white':
                    v.d = u.d + 1
                    v.color = 'grey'
                    Q.append(v)
            u.color = 'black'
        self.printBfs(G, s)
        
    def printBfs(self, G, s):
        for key, u in G.V.iteritems():
            if s.name == u.name:
                print s.name + ' ' + u.name + ' ' + str(u.d)
            elif u.d != 0:
                print s.name + ' ' + u.name + ' ' + str(u.d)

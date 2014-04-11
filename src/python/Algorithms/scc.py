import sys
sys.path.append("../Structures/")
import graph
from dfs import Dfs
from collections import deque

class Scc:

    def execute(self, G):
        dfs = Dfs()
        vertexSeq = dfs.executeNormal(G)
        G.buildTranspGraph()
        sccList = dfs.executeTransp(G, vertexSeq)
        self.printScc(G, sccList)

    def printScc(self, G, sccList):
        for v in sccList:
            print v.getPi().getName()
            if v.getPi() == None:
                print v.getName()
            else:
                print v.getName(),

import sys
sys.path.append("../Structures/")
import graph
from dfs import Dfs
from collections import deque

class Scc:

    def execute(self, G):
        dfs = Dfs()
        dfs.executeNormal(G)
        G.buildTranspGraph()
        dfs.executeTransp(G)
        self.printScc(G, dfs.getSccList())

    def printScc(self, G, sccList):
        for v in sccList:
            if v.getPi() == None:
                print v.getName()
            else:
                print v.getName(),

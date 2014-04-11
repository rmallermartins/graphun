import sys
sys.path.append("../Structures/")
import graph
import dfs
from collections import deque

def execute(V, E, adjList):
    vertexList, pi = dfs.execute(V, adjList)
    ET = graph.transpose(E)
    transpAdjList = graph.makeAdjList(V, ET)
    vertexList.sort()
    sccList, pi = dfs.execute(vertexList.reverse(), transpAdjList)
    printScc(sccList, pi)

def printScc(sccList, pi):
    for v in sccList:
        if pi[v] == None:
            print v
        else:
            print v,
        

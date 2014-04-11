import sys
sys.path.append("../Structures/")
from collections import deque

def execute(V, adjList):
    global pi
    global dist
    global color
    global final
    color = {}
    pi = {}
    time = 0
    vertexList = []
    dist = {}
    final = {}
    
    for u in V:
        color[u] = 'white'
        pi[u] = None
        
    for u in V:
        if color[u] == 'white':
            vertexList = dfsVisit(u, adjList, vertexList, time)
    return vertexList, pi
            
def dfsVisit(u, adjList, vertexList, time):
    time += 1
    color[u] = 'grey'
    dist[u] = time
    
    for v in adjList[u]:
        if color[v] == 'white':
            pi[v] = u
            vertexList = dfsVisit(v, adjList, vertexList, time)
            
    color[u] = 'black'
    time += 1
    final[u] = time
    vertexList.append(u)
    return vertexList

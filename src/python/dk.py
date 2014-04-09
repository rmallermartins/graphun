import heapq
import graph

def execute(V, E, s, adjList):
    global dist
    global pi
    S = []
    Q = []
    
    for v in V:
        heapq.heappush(Q, (dist(v), v))
        
    while Q:
        (u, ) = heap.heappop(Q)
        S.append(u)
        for v in adjList[u]
            graph.relax(u, v, weightList(u, v))

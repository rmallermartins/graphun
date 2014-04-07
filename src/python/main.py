from sys import argv
import bfs
import graph
import scc
import bf

def main():
    vertexes, edges, adjList = graph.makeGraph(argv[2])
    if argv[1] == 'bfs':
        bfs.execute(vertexes, edges, vertexes[0], adjList)
    elif argv[1] == 'scc':
        scc.execute(vertexes, edges, adjList)
    elif argv[1] == 'bf':
        weight = graph.makeWeightList(edges)
        bf.execute(vertexes, edges, vertexes[0], weight)
        
        

if __name__ == "__main__":
    main()

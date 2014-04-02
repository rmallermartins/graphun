from sys import argv
import bfs
import graph
#import scc
import bf

def main():
    vertexes, edges, adjList = graph.makeGraph(argv[2])
    if argv[1] == 'bfs':
        dist = bfs.execute(vertexes, edges, vertexes[0], adjList)
        bfs.printOut(vertexes, edges, vertexes[0], dist)
    #elif argv[1] == 'scc'
    elif argv[1] == 'bf'
        

if __name__ == "__main__":
    main()

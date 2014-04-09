from sys import argv
from bfs import Bfs
from bf import Bf
from graph import Graph

def main():
    G = Graph()
    G.readGraphFile(argv[2])
    
    if argv[1] == 'bfs':
        G.makeAdjLists()
        s = G.getInitVertex()
        bfs = Bfs()
        bfs.execute(G, s)
        
    elif argv[1] == 'scc':
        scc.execute(vertexes, edges, adjList)
        
    elif argv[1] == 'bf':
        bf = Bf()
        s = G.getInitVertex()
        bf.execute(G, s)
        
    elif argv[1] == 'fw':
        W = graph.makeAdjMatrix(vertexes, edges, adjList)
        fw.execute(vertexes, W)
        
        

if __name__ == "__main__":
    main()

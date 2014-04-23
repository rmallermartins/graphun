import sys
sys.path.append("Structures/")
sys.path.append("Algorithms/")
from sys import argv
from bfs import Bfs
from bf import Bf
from fw import Fw
from scc import Scc
from dk import Dk
from graph import Graph

def main():
    G = Graph()
    G.buildGraph(argv[2])
    
    if argv[1] == 'bfs':
        s = G.getInitVertex()
        bfs = Bfs()
        bfs.execute(G, s)
        
    elif argv[1] == 'scc':
        scc = Scc()
        scc.execute(G)
        
    elif argv[1] == 'bf':
        s = G.getInitVertex()
        bf = Bf()
        bf.execute(G, s)
    
    elif argv[1] == 'bfall':
        bf = Bf()
        for key, s in G.getVertexes().iteritems():
            bf.execute(G, s)
    
    elif argv[1] == 'dk':
        s = G.getInitVertex()
        dk = Dk()
        dk.execute(G, s)
    
    elif argv[1] == 'dkall':
        dk = Dk()
        for key, s in G.getVertexes().iteritems():
            dk.execute(G, s)
    
    elif argv[1] == 'fw':
        W = G.getAdjMatrix()
        fw = Fw()
        fw.execute(G, W)
        
        

if __name__ == "__main__":
    main()

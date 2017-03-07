print "Importing Libraries"

import networkx as nx
from sys import stdout

if __name__ == '__main__':

    print "Reading in Graph."
    stdout.flush()
    g = nx.read_edgelist('data/wiki-Talk.txt', create_using=nx.Graph(), nodetype=int)
    
    distribution = dict()
    for i in range (0, 21):
        distribution[i] = 0

    for src in sources:
        visited = set()
        nodes_1 = set(g.neighbors(src))
        nodes_2 = set()

        b = True
        i = 0

        while True:
            if  len(nodes_1) == 0:
                break
            i +=1
            distribution[i] += len(nodes_1)
            nodes_2 = set()
            for node in nodes_1:
                if node not in visited:
                    visited.add(node)
                    nodes_2.update(g.neighbors(node))
            if  len(nodes_2) == 0:
                break
            i += 1
            distribution[i] += len(nodes_2)
            nodes_1 = set()
            for node in nodes_2:
                if node not in visited:
                    visited.add(node)
                    nodes_1.update(g.neighbors(node))

    print "Writing node separation to file"
    stdout.flush()
    with open("data/node_separation.txt", "w+") as file:
        for n, nc in distribution.iteritems()
            file.write("{} {}\n".format(n, nc))


    print "We done here."

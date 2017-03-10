print "Importing Libraries"

import networkx as nx
from sys import stdout

if __name__ == '__main__':

    print "Reading in Graph."
    stdout.flush()
    g = nx.read_edgelist('data/wiki-Talk.txt', create_using=nx.DiGraph(), nodetype=int)
    
    distribution = dict()
    for i in range (0, 21):
        distribution[i] = 0

    print "Performing Separation"
    stdout.flush()
    for src in g.nodes_iter():
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
                visited.add(node)
                nodes_2 = set(g.neighbors(node)) - visited
            if  len(nodes_2) == 0:
                break
            i += 1
            distribution[i] += len(nodes_2)
            nodes_1 = set()
            for node in nodes_2:
                visited.add(node)
                nodes_1 = set(g.neighbors(node)) - visited

    print "Writing node separation to file"
    stdout.flush()
    with open("data/node_separation_2.txt", "w+") as file:
        for n, nc in distribution.iteritems():
            file.write("{} {}\n".format(n, nc))


    print "We done here."

print "Importing Libraries"

import networkx as nx
import sys

def get_top_keys(dictionary, size):
    min_node = -1
    min_value = sys.maxint
    top = dict()
    for (n, b) in dictionary.iteritems():
        if len(top) < size:
            top[n] = b
            if b < min_value:
                min_node = n
                min_value = b
        elif b > min_value:
            del top[min_node]
            top[n] = b
            min_value = sys.maxint
            for (m, c) in top.iteritems():
                if c < min_value:
                    min_node = m
                    min_value = c

    items = sorted(top.iteritems(), key=lambda (k,v): (v,k), reverse=True)

    return items

print "Reading in Graph."
g = nx.read_edgelist('data/wiki-Talk.txt', create_using=nx.DiGraph(), nodetype=int)
print "Graph Imported, analysing and plotting node degrees."


with open("results/degree_top.txt", "w+") as file:
    deg = g.in_degree()
    file.write("Top 100 Nodes by In-degree\n")
    file.write("Node, In-Degree\n")
    for n,p in get_top_keys(deg, 100):
        file.write("{} {}\n".format(n, deg[n]))

    deg = g.out_degree()
    file.write("\nTop 100 Nodes by Out-degree\n")
    file.write("Node, Out-Degree\n")
    for n,p in get_top_keys(deg, 100):
        file.write("{} {}\n".format(n, deg[n]))   
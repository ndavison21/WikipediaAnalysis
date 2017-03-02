print "Importing Libraries"

import networkx as nx
import sys

print "Reading in Graph."
g = nx.read_edgelist('cambridge_net.txt', create_using=nx.DiGraph(), nodetype=int)
print "Graph Imported."

def get_top_keys(dictionary, top):
    items = dictionary.items()
    items.sort(reverse=True, key=lambda x: x[1])
    return items[:top]

bt = nx.betweenness_centrality(g)

print "Printing details of betweeness"
sys.stdout.flush()
for (node, btwn) in get_top_keys(bt, 20):
    print "(node, betweenness): ({},{})".format(node,btwn)
    sys.stdout.flush()
    
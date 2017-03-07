print "Importing Libraries"

import networkx as nx
from sys import stdout

print "Reading in Graph."
stdout.flush()
g = nx.read_edgelist('data/wiki-Talk.txt', create_using=nx.DiGraph(), nodetype=int)
print "Graph Imported."
stdout.flush()

print "Calculating betweenness"
stdout.flush()
bt = nx.betweenness_centrality(g, k=100000)

print "Printing details of betweeness"
stdout.flush()
with open("results/node_betweenness.txt", "w+") as file:
	for (node, btwn) in bt.iteritems():
	    file.write("{} {}\n".format(node,btwn))
    

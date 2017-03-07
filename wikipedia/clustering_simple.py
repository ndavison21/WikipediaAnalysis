print "Importing Libraries"

import networkx as nx
from sys import stdout

print "Reading in Graph."
stdout.flush()
g = nx.read_edgelist('data/wiki-Talk.txt', create_using=nx.Graph(), nodetype=int)
print "Graph Imported."
stdout.flush()

bt = nx.clustering(g)

print "Printing details of clustering"
stdout.flush()
with open("results/node_clustering.txt", "w+") as file:
	for (node, btwn) in bt.iteritems():
	    file.write("{} {}\n".format(node,btwn))


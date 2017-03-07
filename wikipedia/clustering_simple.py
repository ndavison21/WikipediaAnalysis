print "Importing Libraries"

import networkx as nx
from sys import stdout

print "Reading in Graph."
g = nx.read_edgelist('data/wiki-Talk.txt', create_using=nx.Graph(), nodetype=int)
print "Graph Imported."

bt = nx.clustering(g)

print "Printing details of clustering"
stdout.flush()
with open("results/node_clustering.txt", "w+") as file:
	for (node, btwn) in bt:
	    file.write("{} {}\n".format(node,btwn))


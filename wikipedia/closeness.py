print "Importing Libraries"

import networkx as nx
print "Reading in Graph."
g = nx.read_edgelist('wiki-Talk.txt', create_using=nx.DiGraph(), nodetype=int)
print "Graph Imported."

print "Calculating Betweeness Centrality."
bet_cen = nx.betweeness_centrality(g)
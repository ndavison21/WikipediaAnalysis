print "Importing Libraries"

import networkx as nx

print "Reading in Graph."
g = nx.read_edgelist('wiki-Talk.txt', create_using=nx.DiGraph(), nodetype=int)
print "Graph Imported."

print "Need to convert to undirected graph."
g_ud = g.to_undirected()

print "Calculating Clustering Coefficient."
clust_coefficient = nx.average_clustering(g_ud)

print "Calculated. Writing to file"
file = open("results/clust.txt", "w")
file.write("Average Clustering Coefficient is: {}".format(clust_coefficient))
file.close()

print "We Done Here."

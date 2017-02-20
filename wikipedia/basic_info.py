print "Importing Libraries"

import networkx as nx

print "Reading in Graph."
g = nx.read_edgelist('data/wiki-Talk_10000.txt', create_using=nx.DiGraph(), nodetype=int)
print "Graph Imported."

print "Need to convert to undirected graph."
g_ud = g.to_undirected()

print "Writing to file"
file = open("results/basic_info_10000.txt", "w+")
print "Graph Info."
file.write(nx.info(g))
print "Number of Strongly Connected Components."
file.write("SCC: {}\n".format(nx.number_strongly_connected_components(g)))
print "Number of Weakly Connected Components."
file.write("WCC: {}\n".format(nx.number_weakly_connected_components(g)))
print "Average Clustering Coefficient."
file.write("Average Clustering Coefficient: {}\n".format(nx.average_clustering(g_ud)))
file.close()

print "Reading in Graph."
g = nx.read_edgelist('data/wiki-Talk_1000.txt', create_using=nx.DiGraph(), nodetype=int)
print "Graph Imported."

print "Need to convert to undirected graph."
g_ud = g.to_undirected()

print "Writing to file"
file = open("results/basic_info_1000.txt", "w+")
print "Graph Info."
file.write(nx.info(g))
print "Number of Strongly Connected Components."
file.write("SCC: {}\n".format(nx.number_strongly_connected_components(g)))
print "Number of Weakly Connected Components."
file.write("WCC: {}\n".format(nx.number_weakly_connected_components(g)))
print "Average Clustering Coefficient."
file.write("Average Clustering Coefficient: {}\n".format(nx.average_clustering(g_ud)))
file.close()

print "We Done Here."

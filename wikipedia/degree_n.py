print "Importing Libraries"

import networkx as nx
from sys import stdout

print "Reading in Graph."
g = nx.read_edgelist('data/wiki-Talk.txt', create_using=nx.DiGraph(), nodetype=int)
print "Graph Imported, analysing and plotting node degrees."

in_degrees = g.in_degree()
in_values = sorted(set(in_degrees.values()))
in_hist = [in_degrees.values().count(x) for x in range(0,11)]

with open("results/in-degree_bottom.txt", "w+") as file:
	for i in range(0, 11):
		file.write("Nodes with in-degree of {}: {}\n".format(i, in_hist[i]))
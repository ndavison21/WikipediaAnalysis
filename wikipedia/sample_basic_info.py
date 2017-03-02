print "Importing Libraries"
import sys
import networkx as nx

print "Reading in Sample Graph."
sys.stdout.flush()
g = nx.read_edgelist('data/wiki-Talk_rw.txt', create_using=nx.DiGraph(), nodetype=int)
print "Graph Imported, analysing basic info."

file = open("results/sample/basic_info.txt", "a+")

file.write("*** Sample Graph ***\n")
print "Basic Graph Info."
sys.stdout.flush()
file.write(nx.info(g))

print "Reciprocity."
sys.stdout.flush()
reciprocated = 0
for (u,v) in g.edges_iter():
	if g.has_edge(v, u):
		reciprocated = reciprocated + 1
file.write("\nReciprocity: {}\n".format(float(reciprocated)/nx.number_of_edges(g)))
file.flush()
print "Clustering."
sys.stdout.flush()
file.write("Clustering: {}\n".format(nx.average_clustering(g.to_undirected())))

file.close()
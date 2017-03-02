print "Importing Libraries"
import sys
import networkx as nx

print "Reading in Sample Graph."
sys.stdout.flush()
g = nx.read_edgelist('data/wiki-Talk_rw.txt', create_using=nx.DiGraph(), nodetype=int)
print "Graph Imported, analysing and plotting node degrees."

print "Convert to undirected graph."
sys.stdout.flush()
g_ud = g.to_undirected()

file = open("results/sample/basic_info.txt", "w+")

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

file.close()
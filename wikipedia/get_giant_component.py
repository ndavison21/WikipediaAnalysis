print "Importing Libraries"
import sys
import networkx as nx

print "Reading in Sample Graph."
sys.stdout.flush()
g = nx.read_edgelist('data/wiki-Talk_rw.txt', create_using=nx.DiGraph(), nodetype=int)
print "Graph Imported, getting giant component."

g_ud = g.to_undirected()

print "Getting connected subgraphs."
sys.stdout.flush()
connected_subgraphs = nx.connected_component_subgraphs(g_ud)
print "Getting connected giant component."
sys.stdout.flush()
sg = max(connected_subgraphs, key=len)
print "Got connected giant component"

file = open("data/sample_giant_component.txt", "w+")
for u, v in sg.edges_iter():
	if g.has_edge(u, v):
		file.write("{} {}\n".format(u, v))
	if g.has_edge(v, u):
		file.write("{} {}\n".format(v, u))
file.close()

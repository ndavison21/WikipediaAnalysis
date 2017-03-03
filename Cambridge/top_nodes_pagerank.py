from networkx import DiGraph, read_edgelist, pagerank_scipy
from sys import stdout

def get_top_keys(dictionary, top):
	items = dictionary.items()
	items.sort(reverse=True, key=lambda x: x[1])
	return items[:top]

print "Reading in Full Graph."
stdout.flush()
g = read_edgelist('cambridge_net.txt', create_using=DiGraph(), nodetype=int)

print "PageRank."
stdout.flush()

file = open("results/pagerank.txt", "w+")
file.write("Top 100 Nodes by PageRank\n")
pagerank = pagerank_scipy(g)
for node in get_top_keys(pagerank, 100):
	file.write("{}, {}\n".format(node[0], node[1]))
file.close()

print "We Done Here."

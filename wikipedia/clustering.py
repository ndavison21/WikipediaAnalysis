print "Importing Libraries"

import networkx as nx
from multiprocessing import Pool, freeze_support
from sys import stdout
from math import floor
from numpy import histogram

def clust_fun(in_tuple):
	g, sources = in_tuple
	return nx.clustering(g, sources)


if __name__ == '__main__':
	freeze_support()

	print "Reading in Graph."
	stdout.flush()
	g = nx.read_edgelist('data/wiki-Talk.txt', create_using=nx.Graph(), nodetype=int)



	p = Pool()
	num_partitions = len(p._pool)
	nodes = g.nodes()
	size_partitions = int(floor(len(nodes) / num_partitions))

	print num_partitions, "partitions of size", size_partitions
	stdout.flush()

	partitions = list()
	for i in range(0, num_partitions):
		partitions.append(nodes[i*size_partitions:(i+1)*size_partitions-1])


	clusts = p.map(clust_fun, zip([g]*num_partitions, partitions))
	clust = clusts[0]


	for i in range(1,num_partitions):
		for n, nc in clusts[i].items():
			clust[n] = nc

	hist = histogram(clust.values(), bins=10)

	with open("results/clustering_hist.txt", "w+") as file:
		h, e  = hist
		file.write("Values\n")
		for i in h:
			file.write("{}\n".format(i))
		file.write("Edges\n")
		for i in e:
			file.write("{}\n".format(i))

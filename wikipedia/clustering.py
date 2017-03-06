print "Importing Libraries"

import networkx as nx
from multiprocessing import Pool
from functools import partial
from sys import stdout
from math import floor
from numpy import histogram
import itertools


def partitions(nodes, n):
    nodes_iter = iter(nodes)
    while True:
        partition = tuple(itertools.islice(nodes_iter,n))
        if not partition:
            return
        yield partition


if __name__ == '__main__':

	print "Reading in Graph."
	stdout.flush()
	g = nx.read_edgelist('wiki-Talk.txt', create_using=nx.Graph(), nodetype=int)

	clust_fun = partial(nx.clustering, g)

	p = Pool()
	num_partitions = len(p._pool)
	size_partitions = int(len(g) / num_partitions)

	print num_partitions, "partitions of size", size_partitions
	stdout.flush()

	npartitions = list(partitions(g.nodes(), size_partitions))



	clusts = p.imap(clust_fun, npartitions)
	clust = dict()

	for c in clusts:
		for n, nc in c.iteritems():
			clust[n] = nc

	print "Writing node clutsering to file"
	stdout.flush()
	with open("data/node_clustering.txt", "w+") as file:
		for n, nc in clust.iteritems():
			file.write("{} {}\n".format(n, nc))

	print "Creating Histograms"
	stdout.flush()

	hist = histogram(clust.values(), bins=1000)
	with open("results/clustering_hist_1000.txt", "w+") as file:
		h, e  = hist
		file.write("Values\n")
		for i in h:
			file.write("{}\n".format(i))
		file.write("Edges\n")
		for i in e:
			file.write("{}\n".format(i))

	
	hist = histogram(clust.values(), bins=10000)
	with open("results/clustering_hist_10000.txt", "w+") as file:
		h, e  = hist
		file.write("Values\n")
		for i in h:
			file.write("{}\n".format(i))
		file.write("Edges\n")
		for i in e:
			file.write("{}\n".format(i))

	hist = histogram(clust.values(), bins=100000)
	with open("results/clustering_hist_100000.txt", "w+") as file:
		h, e  = hist
		file.write("Values\n")
		for i in h:
			file.write("{}\n".format(i))
		file.write("Edges\n")
		for i in e:
			file.write("{}\n".format(i))
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
	g = nx.read_edgelist('data/wiki-Talk.txt', create_using=nx.Graph(), nodetype=int)

	clust_fun = partial(nx.clustering, g)

	p = Pool()
	num_partitions = len(p._pool)
	size_partitions = int(len(g) / num_partitions)

	print num_partitions, "partitions of size", size_partitions
	stdout.flush()

	npartitions = list(partitions(g.nodes(), size_partitions))

	clusts = p.map(clust_fun, npartitions)

	print "Writing node clutsering to file"
	stdout.flush()
	with open("data/node_clustering.txt", "w+") as file:
		for c in clusts:
			for n, nc in c.iteritems():
				file.write("{} {}\n".format(n, nc))


	print "We done here."
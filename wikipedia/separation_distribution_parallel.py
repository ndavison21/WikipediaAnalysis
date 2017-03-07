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

def separation(g, sources):
	distribution = dict()
	for i in range (0, 21):
		distribution[i] = 0

	for src in sources:
		sys.stdout.flush()

		visited = set()
		nodes_1 = set(g.neighbors(src))
		nodes_2 = set()

		b = True
		i = 0

		while True:
			if  len(nodes_1) == 0:
				break
			i +=1
			distribution[i] += len(nodes_1)
			nodes_2 = set()
			for node in nodes_1:
				if node not in visited:
					visited.add(node)
					nodes_2.update(g.neighbors(node))
			if  len(nodes_2) == 0:
				break
			i += 1
			distribution[i] += len(nodes_2)
			nodes_1 = set()
			for node in nodes_2:
				if node not in visited:
					visited.add(node)
					nodes_1.update(g.neighbors(node))


	return distribution 


if __name__ == '__main__':

	print "Reading in Graph."
	stdout.flush()
	g = nx.read_edgelist('data/wiki-Talk.txt', create_using=nx.Graph(), nodetype=int)

	sep_fun = partial(separation, g)

	p = Pool()
	num_partitions = len(p._pool)
	size_partitions = int(len(g) / num_partitions)

	print num_partitions, "partitions of size", size_partitions
	stdout.flush()

	npartitions = list(partitions(g.nodes(), size_partitions))

	# clusts = p.imap(sep_fun, npartitions)

	print "Writing node separation to file"
	stdout.flush()
	with open("data/node_separation.txt", "w+") as file:
		for c in p.imap_unordered(sep_fun, npartitions):
			for n, nc in c.iteritems():
				file.write("{} {}\n".format(n, nc))


	print "We done here."

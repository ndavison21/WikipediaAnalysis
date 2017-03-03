print "Importing Libraries"

import networkx as nx
from multiprocessing import Pool
import sys
from math import floor
from numpy import histogram

print "Reading in Graph."
sys.stdout.flush()
g = nx.read_edgelist('data/wiki-Talk_rw.txt', create_using=nx.DiGraph(), nodetype=int)

def clustering(sources):
	return nx.clustering(g, sources)

p = Pool()
num_partitions = len(p._pool)
nodes = g.nodes()
size_partitions = int(floor(len(nodes) / num_partitions))

print num_partitions, "partitions of size", size_partitions
sys.stdout.flush()

partitions = list()
for i in range(0, num_partitions):
	partitions.append(nodes[i*size_partitions:(i+1)*size_partitions-1])

print num_partitions, "partitions."
sys.stdout.flush()

clusts = p.map(clustering, partitions)
clust = clusts[0]
for c in clusts:
	for n, nc in c:
		clust[n] = c

hist = histogram(clust, bins=10)

with open("results/clustering_hist.txt", "w+") as fp:
	h, e  = hist
	file.write("Values")
	for i in h:
		file.write("{}\n".format(i))
	file.write("Edges")
	for i in e:
		file.write("{}\n".format(i))
